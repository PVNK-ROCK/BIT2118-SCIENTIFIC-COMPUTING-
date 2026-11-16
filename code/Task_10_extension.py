"""Task 10 extension: (A) change ambient/bracket, (B) break-even production volume."""
import numpy as np
from scipy.optimize import root_scalar

print("=== PART A: change the ambient temperature in the heat-balance model ===")
for amb in (25, 35):
    f = lambda T, amb=amb: T - amb - 10 * np.exp(-T / 20)
    g = lambda T, amb=amb: amb + 10 * np.exp(-T / 20)
    s = root_scalar(f, bracket=[20, 60], method="bisect", xtol=1e-10)
    T, n = 30.0, 0
    while abs(g(T) - T) > 1e-10 and n < 200:
        T, n = g(T), n + 1
    print(f"ambient={amb} C: bisection root={s.root:.6f} C ({s.iterations} its), fixed-point={T:.6f} C ({n} its)")
print("Wider bracket [20, 200] for ambient 25:",
      root_scalar(lambda T: T - 25 - 10*np.exp(-T/20), bracket=[20, 200], method="bisect", xtol=1e-10).iterations, "bisection iterations")

print("\n=== PART B: break-even point for a small factory ===")
# Revenue R(q) = 48 q ; Cost C(q) = 12000 + 20 q + 0.004 q^2   (q = units per month)
profit = lambda q: 48 * q - (12000 + 20 * q + 0.004 * q**2)
print("Profit at q=100:", round(profit(100), 2), "| at q=2000:", round(profit(2000), 2))
low = root_scalar(profit, bracket=[100, 1000], method="bisect", xtol=1e-8)
high = root_scalar(profit, bracket=[3000, 6998], method="bisect", xtol=1e-8)
print(f"First break-even volume : {low.root:.2f} units ({low.iterations} bisection steps)")
print(f"Second break-even volume: {high.root:.2f} units")
q = 500.0
g = lambda q: 12000 / (48 - 20 - 0.004 * q)         # fixed-point form q = F/(p - v - a q)
for _ in range(100):
    q_new = g(q)
    if abs(q_new - q) < 1e-9: break
    q = q_new
print(f"Fixed-point break-even  : {q_new:.2f} units")
qs = np.linspace(0, 7000, 8)
print("Profit at q =", qs.astype(int).tolist(), "->", np.round(profit(qs)).astype(int).tolist())
