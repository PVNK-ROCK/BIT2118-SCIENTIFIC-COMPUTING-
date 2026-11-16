# Task 12: Polynomial and Nonlinear Equation Solving

**Concept:** A nonlinear system has equations that are not all linear. Numerical solvers search for values making every residual close to zero, and different starting guesses can find different solutions.

**Files:** [`code/Task_12_nonlinear_equations.py`](../code/Task_12_nonlinear_equations.py) (given program) · [`code/Task_12_extension.py`](../code/Task_12_extension.py) (parameter change + new real-world case)

---

## 1. Inputs and mathematical operation

- **Input values:** circle x² + y² = 4 and parabola y = x² − 1; starting guesses (1, 1) and (−1, 1).
- **Mathematical operation:** `scipy.optimize.root` solves the two residual equations simultaneously.

## 2. Output of the program

```text
Initial guess: [1.0, 1.0]
Intersection: [1.51748991 1.30277564]
Residuals: [np.float64(-2.4780177909633494e-13), np.float64(-2.4158453015843406e-13)]
Converged: True

Initial guess: [-1.0, 1.0]
Intersection: [-1.51748991  1.30277564]
Residuals: [np.float64(-2.4780177909633494e-13), np.float64(-2.4158453015843406e-13)]
Converged: True
```

## 3. Interpretation of the output

There are two intersection points: **(1.5175, 1.3028)** and **(−1.5175, 1.3028)**, mirror images because both curves are symmetric about the y-axis. The residuals are about 10⁻¹³ and the solver reports convergence. Substituting x² = y + 1 gives y² + y − 3 = 0, whose second root y = −2.30 would need x² < 0, so it has no real intersection. Different starting guesses were needed to find both solutions. There is no graph in this task.

## 4. Changing an input / parameter

**Change made:** the circle radius was changed from 2 to 3, then 1, then 0.5.

```text
r=3.0: 2 intersection(s): [(-1.8364, 2.3723), (1.8364, 2.3723)]
r=1.0: 3 intersection(s): [(-1.0, 0.0), (0.0, -1.0), (1.0, 0.0)]
r=0.5: 0 intersection(s): []
```

**How the result changes:** r = 3 still gives two points (±1.8364, 2.3723). r = 1 gives **three** intersections: (±1, 0) and (0, −1), because the parabola's vertex lies exactly on the circle. r = 0.5 gives **no** intersection, since the circle is too small to touch the parabola (its vertex at y = −1 is outside), so the solver never converges to a valid solution. The number of solutions of a nonlinear system can change with the parameters.

## 5. Modified program for a different but related real-world case

**Case:** Hydrogen-ion concentration and pH of acetic acid (polynomial equilibrium)

**New assumptions**

- Acid dissociation HA ⇌ H⁺ + A⁻ with Ka = 1.8 × 10⁻⁵ (acetic acid, 25 °C), ignoring the water's own ionisation.
- With x = [H⁺]: x²/(C − x) = Ka, so x² + Ka·x − Ka·C = 0, a quadratic solved with `np.roots`. Only the positive root smaller than C is physical.
- Three starting concentrations C = 0.1, 0.01 and 0.001 mol/L.

**Input data:** Ka and concentrations in `code/Task_12_extension.py`.

**Output**

```text
C=0.1 mol/L: roots=[-0.001351  0.001333] -> [H+]=1.3327e-03 mol/L, pH=2.875, ionised=1.33%
C=0.01 mol/L: roots=[-0.000433  0.000415] -> [H+]=4.1536e-04 mol/L, pH=3.382, ionised=4.15%
C=0.001 mol/L: roots=[-0.000143  0.000125] -> [H+]=1.2547e-04 mol/L, pH=3.901, ionised=12.55%
```

**Interpretation:** For 0.1 mol/L the pH is **2.875** with only **1.3 %** of the acid ionised. Diluting the acid raises the pH (3.38 and 3.90) and increases the fraction ionised (4.2 % and 12.5 %): weak acids dissociate more when dilute. Each polynomial has one negative root (rejected as impossible, concentration cannot be negative) and one valid positive root.
