"""Task 15 extension: (A) change step size h, (B) acceleration of a vehicle from speed data."""
import os
import numpy as np
import matplotlib.pyplot as plt

print("=== PART A: change step size h when differentiating sin(x) at x=1 ===")
exact = np.cos(1.0)
for h in (1e-1, 1e-3, 1e-5, 1e-8, 1e-12):
    fwd = (np.sin(1 + h) - np.sin(1)) / h
    cen = (np.sin(1 + h) - np.sin(1 - h)) / (2 * h)
    print(f"h={h:.0e}: forward error={abs(fwd-exact):.2e}, central error={abs(cen-exact):.2e}")

print("\n=== PART B: acceleration of a matatu/bus from speed readings ===")
# Assumption: speed sampled every 2 s as the vehicle leaves a stop and then brakes
t = np.arange(0, 22, 2.0)
v = np.array([0, 2.5, 5.2, 8.0, 10.5, 12.6, 13.8, 14.0, 13.2, 11.0, 7.5])       # m/s
a = np.gradient(v, t)       # central inside, one-sided at ends
for ti, vi, ai in zip(t, v, a):
    print(f"t={ti:4.0f} s  speed={vi:5.1f} m/s  acceleration={ai:6.2f} m/s^2")
print(f"Max acceleration {a.max():.2f} m/s^2 at t={t[a.argmax()]:.0f} s; hardest braking {a.min():.2f} m/s^2 at t={t[a.argmin()]:.0f} s")
fig, ax = plt.subplots()
ax.plot(t, v, "o-", label="Speed (m/s)"); ax.plot(t, a, "s--", label="Acceleration (m/s^2)")
ax.axhline(0, lw=0.8); ax.set_xlabel("Time (s)"); ax.legend(); ax.grid(True)
ax.set_title("Speed and estimated acceleration")
os.makedirs("images", exist_ok=True)
fig.savefig("images/task_15_acceleration_extension.png", dpi=150, bbox_inches="tight")
