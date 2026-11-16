"""Task 6 extension: (A) change totals, (B) mesh-current analysis of an electrical circuit."""
import numpy as np

A = np.array([[4.0, 2.0], [8.0, 12.0]])
print("=== PART A: change the observed totals ===")
for cpu, mem in ((20, 72), (22, 80), (20, 40)):
    x = np.linalg.solve(A, np.array([cpu, mem], dtype=float)) + 0.0
    x[np.abs(x) < 1e-12] = 0.0
    print(f"CPU={cpu}, Memory={mem}: Type A={x[0]:.3f}, Type B={x[1]:.3f}")
print("Determinant of A:", round(np.linalg.det(A), 3), "(non-zero -> unique solution)")

print("\n=== PART B: three-loop DC circuit (Kirchhoff's voltage law) ===")
# Unknowns: mesh currents I1, I2, I3 (amps). Resistances in ohms, sources in volts.
# Loop 1: 10*I1 - 4*I2         = 12
# Loop 2: -4*I1 + 12*I2 - 5*I3 = 0
# Loop 3: -5*I2 + 9*I3         = -6
R = np.array([[10., -4., 0.], [-4., 12., -5.], [0., -5., 9.]])
V = np.array([12., 0., -6.])
I = np.linalg.solve(R, V)
print("Mesh currents (A):", np.round(I, 4))
print("Residual norm:", np.linalg.norm(V - R @ I))
print(f"Current through shared 4-ohm resistor: {I[0]-I[1]:.4f} A")
print(f"Power lost in that resistor: {4*(I[0]-I[1])**2:.4f} W")
