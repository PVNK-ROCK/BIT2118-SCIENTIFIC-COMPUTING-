# Task 4: Floating-Point Arithmetic and Numerical Errors

**Concept:** Computers store most real numbers approximately in binary, so results carry round-off error. Absolute error = |true − approx|; relative error = absolute error / |true|.

**Files:** [`code/Task_04_numerical_errors.py`](../code/Task_04_numerical_errors.py) (given program) · [`code/Task_04_extension.py`](../code/Task_04_extension.py) (parameter change + new real-world case)

---

## 1. Inputs and mathematical operation

- **Input values:** 0.1 + 0.2 compared with 0.3; √2 compared with 1.414; x = 10⁻⁴, 10⁻⁸, 10⁻¹².
- **Mathematical operations:** equality test vs `np.isclose`, absolute/relative error, and two algebraically equal formulas for (√(1+x) − 1)/x.

## 2. Output of the program

```text
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00021356
Relative error: 0.01510114%
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
```

## 3. Interpretation of the output

- `0.1 + 0.2` gives `0.30000000000000004`, so `== 0.3` is **False**, but `np.isclose` (tolerance-based) gives **True**. Never test floating-point numbers for exact equality.
- Using 1.414 for √2 gives an absolute error of 0.00021356 and a relative error of 0.0151 %, matching the hand calculation in the brief.
- For small x the **direct** formula loses digits: at x = 10⁻¹² it prints 0.50004445 while the correct value is 0.5. The **stable** formula (rationalised, no subtraction of nearly equal numbers) stays correct. The direct formula suffers *catastrophic cancellation*.

## 4. Changing an input / parameter

**Change made:** (a) the approximation of √2 was refined (1.414 → 1.4142 → 1.41421); (b) x was made even smaller (10⁻¹⁴ and 10⁻¹⁶).

```text
approx=1.414: absolute error=0.00021356, relative error=0.015101%
approx=1.4142: absolute error=0.00001356, relative error=0.000959%
approx=1.41421: absolute error=0.00000356, relative error=0.000252%
x=1e-14: direct=0.488498, stable=0.500000
x=1e-16: direct=0.000000, stable=0.500000
```

**How the result changes:** More correct digits reduce the error roughly in proportion (relative error 0.0151 % → 0.00096 % → 0.00025 %). Making x smaller makes the direct formula *worse*: at 10⁻¹⁴ it is about 2.3 % wrong, and at 10⁻¹⁶ it returns **0** because `1 + x` rounds to exactly 1 and the subtraction wipes out all information. The stable formula still gives 0.5. Smaller step ≠ better result when round-off dominates.

## 5. Modified program for a different but related real-world case

**Case:** Accumulated round-off in a mobile-money transaction-fee ledger

**New assumptions**

- 1,000,000 transactions each charge a fee of exactly 0.10 currency units, so the true total is 100,000.00.
- Three methods are compared: naive `+=` in floating point, `math.fsum` (error-compensated), and `Decimal` (exact decimal arithmetic).

**Input data:** Fee = 0.10, count = 1,000,000 (defined in `code/Task_04_extension.py`).

**Output**

```text
Naive float sum   : 100000.0000013329
math.fsum         : 100000.0000000000
Decimal (exact)   : 100000.00
Naive error       : 1.333e-06
naive == 100000 ? False | np.isclose ? True
```

**Interpretation:** The naive sum is **100000.0000013329**: off by 1.3 × 10⁻⁶, and `== 100000` is False. Each addition of 0.1 introduces a tiny error and they accumulate over a million additions. `math.fsum` and `Decimal` give the exact total. In banking and accounting software, money should be stored as integers (cents) or `Decimal`, and floats should be compared with a tolerance.
