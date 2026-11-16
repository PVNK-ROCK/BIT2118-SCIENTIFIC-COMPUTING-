"""Task 14 extension: (A) change the model, (B) logistic growth of app users."""
import os
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

print("=== PART A: change the model (degree 1, 2, 3) for the server data ===")
users = np.array([50, 100, 150, 200, 250, 300, 350.])
resp = np.array([82, 95, 115, 145, 185, 238, 305.])
for deg in (1, 2, 3):
    coef = np.polyfit(users, resp, deg)
    pred = np.polyval(coef, users)
    rmse = np.sqrt(np.mean((resp - pred)**2))
    print(f"degree {deg}: RMSE={rmse:.2f} ms, prediction at 400 users={np.polyval(coef, 400):.1f} ms")

print("\n=== PART B: logistic growth of mobile-app users (illustrative data) ===")
month = np.arange(0, 12, dtype=float)
users_k = np.array([1.1, 1.6, 2.4, 3.5, 5.0, 7.2, 9.8, 12.5, 15.0, 17.1, 18.6, 19.5])   # thousands
def logistic(t, K, r, t0):
    return K / (1 + np.exp(-r * (t - t0)))
p, cov = curve_fit(logistic, month, users_k, p0=[20, 0.5, 6])
K, r, t0 = p
err = np.sqrt(np.diag(cov))
pred = logistic(month, *p)
print(f"Capacity K={K:.2f}k (+/-{err[0]:.2f}), growth rate r={r:.3f}/month, midpoint t0={t0:.2f} months")
print(f"RMSE={np.sqrt(np.mean((users_k-pred)**2)):.3f}k users")
print(f"Forecast month 15: {logistic(15, *p):.2f}k users; month 24: {logistic(24, *p):.2f}k users")
tp = np.linspace(0, 20, 300)
plt.scatter(month, users_k, label="Observed"); plt.plot(tp, logistic(tp, *p), label="Logistic fit")
plt.axhline(K, ls="--", lw=0.8, label="Estimated capacity")
plt.xlabel("Month"); plt.ylabel("Users (thousands)"); plt.title("Logistic growth of app users")
plt.legend(); plt.grid(True)
os.makedirs("images", exist_ok=True)
plt.savefig("images/task_14_logistic_extension.png", dpi=150, bbox_inches="tight")
