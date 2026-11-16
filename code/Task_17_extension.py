"""Task 17 extension: (A) change step size h, (B) SIR epidemic model with Euler."""
import os
import numpy as np
import matplotlib.pyplot as plt

print("=== PART A: change step size in Newton cooling (k=0.12, exact T(30)=26.78 C) ===")
k, Ta, T0 = 0.12, 25.0, 90.0
exact30 = Ta + (T0 - Ta) * np.exp(-k * 30)
for h in (10.0, 5.0, 1.0, 0.1):
    n = int(round(30 / h)); T = T0
    for _ in range(n):
        T += h * (-k * (T - Ta))
    print(f"h={h:>4}: Euler T(30)={T:8.3f} C, error={abs(T-exact30):.4f} C")
T = T0
for _ in range(2):                      # h=20 -> 1-k*h = -1.4 (|.|>1 -> unstable)
    T += 20 * (-k * (T - Ta))
print("h=20 (unstable, 2 steps -> t=40 min):", round(T, 2), "C  (should be near 25 C!)")

print("\n=== PART B: SIR epidemic model ===")
# Assumptions: population 1000, one infected person, beta=0.3/day, gamma=0.1/day (R0 = 3)
N, beta, gamma, h, days = 1000.0, 0.30, 0.10, 0.5, 160
steps = int(days / h)
S = np.zeros(steps + 1); I = np.zeros(steps + 1); R = np.zeros(steps + 1)
S[0], I[0] = N - 1, 1
for i in range(steps):
    dS = -beta * S[i] * I[i] / N
    dR = gamma * I[i]
    S[i+1] = S[i] + h * dS
    I[i+1] = I[i] + h * (-dS - dR)
    R[i+1] = R[i] + h * dR
t = np.arange(steps + 1) * h
print(f"Peak infections: {I.max():.0f} people on day {t[I.argmax()]:.1f}")
print(f"Total ever infected (final R): {R[-1]:.0f} of {N:.0f} ({R[-1]/N:.1%})")
print(f"Susceptible left: {S[-1]:.0f}")
plt.plot(t, S, label="Susceptible"); plt.plot(t, I, label="Infected"); plt.plot(t, R, label="Recovered")
plt.xlabel("Day"); plt.ylabel("People"); plt.title("SIR epidemic model (Euler, h=0.5 day)")
plt.legend(); plt.grid(True)
os.makedirs("images", exist_ok=True)
plt.savefig("images/task_17_sir_extension.png", dpi=150, bbox_inches="tight")
