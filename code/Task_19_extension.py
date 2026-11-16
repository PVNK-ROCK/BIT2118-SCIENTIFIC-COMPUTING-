"""Task 19 extension: (A) change constraint & costs, (B) maximise factory profit."""
import numpy as np
from scipy.optimize import minimize

def solve(capacity_needed, cost_a, cost_b):
    res = minimize(lambda z: cost_a*z[0] + cost_b*z[1], x0=[5, 3], method="SLSQP",
                   bounds=[(0, None), (0, None)],
                   constraints={"type": "ineq", "fun": lambda z: 100*z[0] + 170*z[1] - capacity_needed})
    return res

print("=== PART A: change the required capacity and the price of Type B ===")
for cap, ca, cb in ((1000, 12, 18), (1500, 12, 18), (1000, 12, 22)):
    r = solve(cap, ca, cb)
    print(f"capacity>={cap}, cost A={ca}, B={cb}: A={r.x[0]:.3f}, B={r.x[1]:.3f}, cost={r.fun:.2f}")

print("\n=== PART B: production planning - maximise profit ===")
# Products: chairs (x) earn 40 profit each, tables (y) earn 30.
# Machine time: 2x + y <= 100 h ; Labour: x + y <= 80 h ; chairs limited by demand x <= 40
neg_profit = lambda z: -(40*z[0] + 30*z[1])
cons = [{"type": "ineq", "fun": lambda z: 100 - 2*z[0] - z[1]},
        {"type": "ineq", "fun": lambda z: 80 - z[0] - z[1]}]
r = minimize(neg_profit, x0=[10, 10], method="SLSQP", bounds=[(0, 40), (0, None)], constraints=cons)
print(f"Chairs={r.x[0]:.2f}, Tables={r.x[1]:.2f}, Max profit={-r.fun:.2f}")
print(f"Machine hours used: {2*r.x[0]+r.x[1]:.2f}/100, labour hours used: {r.x[0]+r.x[1]:.2f}/80")
print("Integer check (best whole numbers):",
      max(((40*a+30*b, a, b) for a in range(41) for b in range(81) if 2*a+b <= 100 and a+b <= 80)))
