"""Task 16 extension: (A) change sampling interval, (B) flood volume from a river hydrograph."""
import numpy as np
from scipy.integrate import simpson

print("=== PART A: change sampling interval for P(t) = 1.2 + 0.6*sin(pi t/12) over 12 h ===")
P = lambda t: 1.2 + 0.6 * np.sin(np.pi * t / 12)
exact = 1.2 * 12 + 0.6 * 24 / np.pi          # analytical integral = 18.984 kWh
print(f"Exact energy: {exact:.4f} kWh")
for step in (6, 3, 2, 1):
    t = np.arange(0, 12 + 1e-9, step)
    tr, si = np.trapezoid(P(t), t), simpson(P(t), x=t)
    print(f"step {step} h: trapezoid={tr:.4f} (err {abs(tr-exact):.4f}), simpson={si:.4f} (err {abs(si-exact):.4f})")

print("\n=== PART B: water volume passing a river gauge during a storm ===")
# Assumption: discharge (m^3/s) logged every 30 minutes for 6 hours
t_h = np.arange(0, 6.5, 0.5)
q = np.array([12, 15, 28, 55, 90, 120, 105, 82, 64, 50, 40, 31, 25])
t_s = t_h * 3600
vol_tr = np.trapezoid(q, t_s); vol_si = simpson(q, x=t_s)
print(f"Volume (trapezoid): {vol_tr:,.0f} m^3 = {vol_tr/1e6:.3f} million m^3")
print(f"Volume (Simpson)  : {vol_si:,.0f} m^3 = {vol_si/1e6:.3f} million m^3")
print(f"Peak flow {q.max()} m^3/s at t={t_h[q.argmax()]} h; mean flow {vol_si/t_s[-1]:.1f} m^3/s")
base = q[0] * t_s[-1]
print(f"Storm excess over base flow (12 m^3/s): {(vol_si-base)/1e6:.3f} million m^3")
