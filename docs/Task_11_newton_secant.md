# Task 11: Root Finding: Newton-Raphson and Secant Methods

**Concept:** Newton-Raphson uses xₙ₊₁ = xₙ − f(xₙ)/f′(xₙ) (the tangent line). The secant method replaces f′ with a slope through the last two points, so no derivative is needed.

**Files:** [`code/Task_11_newton_secant.py`](../code/Task_11_newton_secant.py) (given program) · [`code/Task_11_extension.py`](../code/Task_11_extension.py) (parameter change + new real-world case)

---

## 1. Inputs and mathematical operation

- **Input values:** cash flows −10,000, 3,000, 3,500, 4,000, 2,500 over 5 years; start x₀ = 0.10 (Newton) and x₀ = 0.05, x₁ = 0.20 (secant).
- **Mathematical operation:** find the rate r where NPV(r) = Σ CFₜ/(1+r)ᵗ = 0, the internal rate of return (IRR).

## 2. Output of the program

```text
IRR using Newton-Raphson: 11.542461%  (4 iterations)
IRR using Secant method:  11.542461%  (7 iterations)
NPV at Newton solution:   0.000000
```

## 3. Interpretation of the output

Both methods give an IRR of **11.5425 %**, so NPV ≈ 0 at that rate. Newton converged in **4** iterations and the secant method in **7**: Newton is faster per step because it uses the exact derivative, while the secant method avoids having to code a derivative. The project is worthwhile if the required return is below 11.54 %. There is no graph in this task.

## 4. Changing an input / parameter

**Change made:** the initial investment 10,000 → **12,000**, and the Newton starting guess 0.10 → **0.90**.

```text
investment=10000, x0=0.1: IRR=11.5425%, iterations=4
investment=12000, x0=0.1: IRR=3.3298%, iterations=5
investment=12000, x0=0.9: IRR=3.3298%, iterations=9
```

**How the result changes:** The IRR drops sharply to **3.33 %**: paying more at the start for the same inflows lowers the return. A distant starting guess (0.9) still reaches the same root but needs 9 iterations instead of 5, so Newton's method converges quickly only when the start is reasonably close to the root.

## 5. Modified program for a different but related real-world case

**Case:** True interest rate of an instalment loan

**New assumptions**

- A loan of 5,000 is repaid with 24 monthly payments of 230.
- The monthly rate i satisfies 5000 = 230·(1 − (1+i)⁻²⁴)/i; the secant method is used because the derivative is awkward.
- Starting values 0.5 % and 3 % per month.

**Input data:** P = 5000, payment = 230, n = 24 in `code/Task_11_extension.py`.

**Output**

```text
Monthly rate (secant): 0.8071% after 6 iterations
Nominal annual rate  : 9.69%
Effective annual rate: 10.13%
Total repaid: 5520, interest paid: 520
```

**Interpretation:** The loan costs **0.807 % per month**, which is a nominal annual rate of **9.69 %** and an *effective* annual rate of **10.13 %** (compounding). Total interest paid is 520 on 5,000 borrowed. Borrowers can use this to compare loan offers quoted in different ways.
