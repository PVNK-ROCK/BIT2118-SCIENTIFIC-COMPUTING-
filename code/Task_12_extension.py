"""Task 12 extension: (A) change the circle radius, (B) weak-acid equilibrium polynomial."""
import numpy as np
from scipy.optimize import root

print("=== PART A: change the circle radius r (circle x^2+y^2=r^2, parabola y=x^2-1) ===")
for r in (3.0, 1.0, 0.5):
    eq = lambda z, r=r: [z[0]**2 + z[1]**2 - r**2, z[1] - (z[0]**2 - 1)]
    found = set()
    for guess in ([1, 1], [-1, 1], [0.5, -1], [2, 2], [-2, -2], [0, -0.9], [0.8, 0.5]):
        s = root(eq, guess)
        if s.success and np.max(np.abs(eq(s.x))) < 1e-9:
            found.add((round(float(s.x[0]), 4) + 0.0, round(float(s.x[1]), 4) + 0.0))
    print(f"r={r}: {len(found)} intersection(s): {sorted(found)}")

print("\n=== PART B: pH of acetic acid (polynomial equilibrium equation) ===")
# HA <-> H+ + A- ; Ka = x^2 / (C - x)  ->  x^2 + Ka*x - Ka*C = 0 ;  x = [H+]
Ka = 1.8e-5
for C in (0.10, 0.01, 0.001):
    roots = np.roots([1, Ka, -Ka * C])
    x = roots[(roots > 0) & (roots < C)].real[0]
    print(f"C={C} mol/L: roots={np.round(roots, 6)} -> [H+]={x:.4e} mol/L, pH={-np.log10(x):.3f}, ionised={x/C:.2%}")
