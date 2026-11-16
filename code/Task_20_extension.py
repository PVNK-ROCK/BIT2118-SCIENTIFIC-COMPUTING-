"""Task 20 extension: (A) change parameters & N, (B) project deadline risk."""
import os, math
import numpy as np
import matplotlib.pyplot as plt

print("=== PART A: change capacity, standard deviation and number of simulations ===")
for cap, sd, N in ((1000, 120, 100_000), (1100, 120, 100_000), (1000, 180, 100_000), (1000, 120, 1_000)):
    rng = np.random.default_rng(42)
    p = (rng.normal(850, sd, N) > cap).mean()
    exact = 0.5 * math.erfc((cap - 850) / (sd * math.sqrt(2)))
    print(f"capacity={cap}, sd={sd}, N={N:>7,}: simulated={p:.4%}, exact normal tail={exact:.4%}")

print("\n=== PART B: probability a 3-stage software project misses a 60-day deadline ===")
# Assumed triangular durations (min, most likely, max) in days
stages = {"Design": (8, 12, 20), "Build": (20, 28, 45), "Test": (8, 12, 25)}
rng = np.random.default_rng(7)
N = 200_000
total = sum(rng.triangular(a, m, b, N) for a, m, b in stages.values())
deadline = 60
print(f"Mean total duration: {total.mean():.2f} days (std {total.std():.2f})")
print(f"Probability of finishing within {deadline} days: {(total <= deadline).mean():.2%}")
print(f"Probability of missing the deadline: {(total > deadline).mean():.2%}")
print(f"90th percentile duration: {np.percentile(total, 90):.1f} days")
plt.hist(total, bins=60, density=True, alpha=0.8)
plt.axvline(deadline, color="r", ls="--", label="Deadline (60 days)")
plt.xlabel("Total project duration (days)"); plt.ylabel("Probability density")
plt.title("Monte Carlo simulation of project duration"); plt.legend(); plt.grid(True)
os.makedirs("images", exist_ok=True)
plt.savefig("images/task_20_project_risk_extension.png", dpi=150, bbox_inches="tight")
