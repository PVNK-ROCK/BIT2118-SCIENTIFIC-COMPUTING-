# Task 6: Solution of Systems of Linear Equations

**Concept:** A linear system is written Ax = b. `np.linalg.solve` finds x so that A·x reproduces b.

**Files:** [`code/Task_06_linear_systems.py`](../code/Task_06_linear_systems.py) (given program) · [`code/Task_06_extension.py`](../code/Task_06_extension.py) (parameter change + new real-world case)

---

## 1. Inputs and mathematical operation

- **Input values:** A = [[4, 2], [8, 12]] (CPU and memory per server type) and b = [20, 72] (total CPU and memory in use).
- **Mathematical operation:** solve 4x + 2y = 20 and 8x + 12y = 72 for x (Type A servers) and y (Type B servers); verify with the residual b − Ax.

## 2. Output of the program

```text
Type A servers: 3
Type B servers: 4
Verification A @ solution: [20. 72.]
Residual: [0. 0.]
Residual norm: 0.0
```

## 3. Interpretation of the output

There are **3 Type A servers and 4 Type B servers**. Check: 4(3) + 2(4) = 20 CPU units and 8(3) + 12(4) = 72 GB. The residual is exactly zero, so the solution satisfies both equations. There is no graph in this task.

## 4. Changing an input / parameter

**Change made:** the observed totals were changed to (22 CPU, 80 GB) and (20 CPU, 40 GB).

```text
CPU=20, Memory=72: Type A=3.000, Type B=4.000
CPU=22, Memory=80: Type A=3.250, Type B=4.500
CPU=20, Memory=40: Type A=5.000, Type B=0.000
Determinant of A: 32.0 (non-zero -> unique solution)
```

**How the result changes:** With (22, 80) the answer becomes 3.25 and 4.5 servers: you cannot have a fraction of a server, so the readings are inconsistent with whole machines (measurement error or a third server type). With (20, 40) the answer is 5 Type A and **0** Type B. The determinant of A is 32 (non-zero), so a unique solution always exists; only its meaning changes with b.

## 5. Modified program for a different but related real-world case

**Case:** Mesh-current analysis of a DC electrical circuit

**New assumptions**

- Three loops with mesh currents I₁, I₂, I₃ (clockwise positive); resistances in ohms, sources in volts.
- Kirchhoff's voltage law gives: 10I₁ − 4I₂ = 12, −4I₁ + 12I₂ − 5I₃ = 0, −5I₂ + 9I₃ = −6.

**Input data:** Coefficient matrix R and source vector V in `code/Task_06_extension.py`.

**Output**

```text
Mesh currents (A): [ 1.277   0.1924 -0.5598]
Residual norm: 9.992007221626409e-16
Current through shared 4-ohm resistor: 1.0845 A
Power lost in that resistor: 4.7050 W
```

**Interpretation:** I₁ = 1.277 A, I₂ = 0.192 A and **I₃ = −0.560 A**. The negative sign means loop 3's current flows opposite to the assumed clockwise direction. The current through the resistor shared by loops 1 and 2 is I₁ − I₂ = 1.0845 A, dissipating P = I²R ≈ 4.7 W. The residual is about 10⁻¹⁵, so the solution is numerically exact.
