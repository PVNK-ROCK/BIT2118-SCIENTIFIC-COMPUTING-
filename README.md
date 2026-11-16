# BIT 2118: Scientific Computing: Group Work (Tasks 2-20)

> **Student:** _Your name_ · **Reg. No.:** _Your registration number_ · **Group:** _Group name/number_
> (Discussions were done as group work; this repository is my own individual submission.)

Each task contains: (1) the inputs and mathematical operation, (2) the program output, (3) an interpretation in words
(including the graph where there is one), (4) a change of at least one input/parameter with an explanation of how the
result changes, and (5) a modified program solving a different, related real-world case with its assumptions,
input data, output and interpretation.

## Task index

| Task | Documentation | Given program | Modified program | New real-world case |
|---|---|---|---|---|
| 2 | [NumPy Arrays and Numerical Computation](docs/Task_02_numpy_arrays.md) | `code/Task_02_numpy_arrays.py` | `code/Task_02_extension.py` | Soil-moisture monitoring for a farm (IoT sensor grid) |
| 3 | [Mathematical Functions and Vectorization](docs/Task_03_vectorization.md) | `code/Task_03_vectorization.py` | `code/Task_03_extension.py` | Annual energy yield of a rooftop solar panel (8,760 hourly values) |
| 4 | [Floating-Point Arithmetic and Numerical Errors](docs/Task_04_numerical_errors.md) | `code/Task_04_numerical_errors.py` | `code/Task_04_extension.py` | Accumulated round-off in a mobile-money transaction-fee ledger |
| 5 | [Matrix Algebra and Matrix Operations](docs/Task_05_matrix_algebra.md) | `code/Task_05_matrix_algebra.py` | `code/Task_05_extension.py` | Forward kinematics of a 2-link robot arm |
| 6 | [Solution of Systems of Linear Equations](docs/Task_06_linear_systems.md) | `code/Task_06_linear_systems.py` | `code/Task_06_extension.py` | Mesh-current analysis of a DC electrical circuit |
| 7 | [Gaussian Elimination and LU Decomposition](docs/Task_07_gaussian_lu.md) | `code/Task_07_gaussian_lu.py` | `code/Task_07_extension.py` | Displacements of a spring-mass structure under three load cases |
| 8 | [Iterative Methods for Linear Systems](docs/Task_08_iterative_linear.md) | `code/Task_08_iterative_linear.py` | `code/Task_08_extension.py` | Steady-state heat conduction along a metal rod with 20 interior points |
| 9 | [Eigenvalues and Eigenvectors](docs/Task_09_eigenvalues.md) | `code/Task_09_eigenvalues.py` | `code/Task_09_extension.py` | PageRank of a 5-page website |
| 10 | [Root Finding: Bisection and Fixed-Point Methods](docs/Task_10_bisection_fixed_point.md) | `code/Task_10_bisection_fixed_point.py` | `code/Task_10_extension.py` | Break-even production volume of a small factory |
| 11 | [Root Finding: Newton-Raphson and Secant Methods](docs/Task_11_newton_secant.md) | `code/Task_11_newton_secant.py` | `code/Task_11_extension.py` | True interest rate of an instalment loan |
| 12 | [Polynomial and Nonlinear Equation Solving](docs/Task_12_nonlinear_equations.md) | `code/Task_12_nonlinear_equations.py` | `code/Task_12_extension.py` | Hydrogen-ion concentration and pH of acetic acid (polynomial equilibrium) |
| 13 | [Interpolation](docs/Task_13_interpolation.md) | `code/Task_13_interpolation.py` | `code/Task_13_extension.py` | Battery state-of-charge from measured voltage (lookup table) |
| 14 | [Curve Fitting and Approximation](docs/Task_14_curve_fitting.md) | `code/Task_14_curve_fitting.py` | `code/Task_14_extension.py` | Logistic growth of mobile-app users |
| 15 | [Numerical Differentiation](docs/Task_15_numerical_differentiation.md) | `code/Task_15_numerical_differentiation.py` | `code/Task_15_extension.py` | Acceleration of a bus from its speed readings |
| 16 | [Numerical Integration](docs/Task_16_numerical_integration.md) | `code/Task_16_numerical_integration.py` | `code/Task_16_extension.py` | Total water volume passing a river gauge during a storm |
| 17 | [Ordinary Differential Equations: Euler Method](docs/Task_17_euler_ode.md) | `code/Task_17_euler_ode.py` | `code/Task_17_extension.py` | SIR epidemic model (Susceptible-Infected-Recovered) |
| 18 | [Numerical Solution of ODEs Using SciPy](docs/Task_18_scipy_ode.md) | `code/Task_18_scipy_ode.py` | `code/Task_18_extension.py` | Car suspension: a second-order ODE (mass-spring-damper) |
| 19 | [Numerical Optimization](docs/Task_19_optimization.md) | `code/Task_19_optimization.py` | `code/Task_19_extension.py` | Production planning: maximise profit |
| 20 | [Random Numbers and Monte Carlo Methods](docs/Task_20_monte_carlo.md) | `code/Task_20_monte_carlo.py` | `code/Task_20_extension.py` | Project deadline risk (three-stage software project) |

## Repository structure

```text
.
├── README.md
├── requirements.txt
├── code/        # Task_XX_*.py (given solution) and Task_XX_extension.py (parameter change + new case)
├── docs/        # Task_XX_*.md write-ups (inputs, output, interpretation, changes, new case)
└── images/      # graphs produced by the programs
```

## How to run

```bash
pip install -r requirements.txt
# run from the repository root so the graphs are saved in ./images
python code/Task_02_numpy_arrays.py
python code/Task_02_extension.py
```

Scripts that draw graphs call `plt.show()`; the same figure is also saved to `images/`. Task 16 uses `np.trapezoid`,
which needs **NumPy 2.0 or newer** (use `np.trapz` on older versions). Timings in Tasks 3 and 7 vary between computers.
