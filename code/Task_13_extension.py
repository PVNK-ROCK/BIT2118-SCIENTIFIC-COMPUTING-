"""Task 13 extension: (A) change the sampling interval, (B) battery state-of-charge lookup."""
import os
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

print("=== PART A: change sampling interval for a known smooth curve ===")
f = lambda t: 20 + 6 * np.sin(np.pi * (t - 8) / 12)       # 'true' temperature curve
fine = np.linspace(8, 14, 601)
for step in (1.0, 2.0, 3.0):
    t = np.arange(8, 14 + 1e-9, step)
    lin = interp1d(t, f(t))(fine); cub = CubicSpline(t, f(t))(fine)
    print(f"samples every {step} h: max error linear={np.max(abs(lin - f(fine))):.4f} C, cubic={np.max(abs(cub - f(fine))):.4f} C")

print("\n=== PART B: battery state-of-charge from measured voltage ===")
# Assumption: a Li-ion cell discharge table (voltage rises with charge)
volt = np.array([3.00, 3.30, 3.50, 3.60, 3.70, 3.80, 3.95, 4.10, 4.20])
soc = np.array([0, 5, 15, 30, 45, 60, 80, 95, 100], dtype=float)
lin, cub = interp1d(volt, soc), CubicSpline(volt, soc)
for v in (3.45, 3.75, 4.00):
    print(f"Measured {v:.2f} V -> linear SOC={float(lin(v)):.1f} %, cubic SOC={float(cub(v)):.1f} %")
v_plot = np.linspace(3.0, 4.2, 200)
plt.scatter(volt, soc, label="Lookup table")
plt.plot(v_plot, lin(v_plot), label="Linear"); plt.plot(v_plot, cub(v_plot), label="Cubic spline")
plt.xlabel("Cell voltage (V)"); plt.ylabel("State of charge (%)")
plt.title("Battery voltage to state-of-charge lookup"); plt.legend(); plt.grid(True)
os.makedirs("images", exist_ok=True)
plt.savefig("images/task_13_battery_extension.png", dpi=150, bbox_inches="tight")
