"""Task 18 extension: (A) change R and C, (B) vehicle suspension (damped spring-mass)."""
import os
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

print("=== PART A: change R and C of the RC circuit (Vs = 5 V) ===")
for R, C in ((1000, 0.001), (1000, 0.0005), (2000, 0.001)):
    sol = solve_ivp(lambda t, V: [(5 - V[0]) / (R * C)], (0, 5), [0.0], rtol=1e-9, atol=1e-11,
                    dense_output=True)
    tau = R * C
    print(f"R={R} ohm, C={C} F: tau={tau:.4f} s, V(tau)={float(sol.sol(tau)[0]):.3f} V (63.2% of 5 = 3.161), V(5 s)={sol.y[0,-1]:.4f} V")

print("\n=== PART B: car suspension (second-order ODE as a first-order system) ===")
# m x'' + c x' + k x = 0 ; assumed m=400 kg (quarter car), k=16000 N/m, initial bump x0=0.08 m
m, k = 400.0, 16000.0
def run(c):
    f = lambda t, y: [y[1], -(c * y[1] + k * y[0]) / m]
    return solve_ivp(f, (0, 3), [0.08, 0.0], t_eval=np.linspace(0, 3, 600), rtol=1e-9, atol=1e-11)
critical = 2 * np.sqrt(k * m)
print(f"Critical damping coefficient: {critical:.0f} N s/m")
plt.figure()
for c, label in ((800, "Worn shock absorber (c=800)"), (3200, "Good shock absorber (c=3200)"), (6400, "Critically damped (c=6400)")):
    s = run(c)
    settle = s.t[np.where(np.abs(s.y[0]) > 0.004)[0][-1]] if np.any(np.abs(s.y[0]) > 0.004) else 0
    print(f"c={c}: damping ratio={c/critical:.2f}, min displacement={s.y[0].min():.4f} m, time to settle within 4 mm = {settle:.2f} s")
    plt.plot(s.t, s.y[0], label=label)
plt.axhline(0, lw=0.8); plt.xlabel("Time (s)"); plt.ylabel("Displacement (m)")
plt.title("Suspension response after hitting a bump"); plt.legend(); plt.grid(True)
os.makedirs("images", exist_ok=True)
plt.savefig("images/task_18_suspension_extension.png", dpi=150, bbox_inches="tight")
