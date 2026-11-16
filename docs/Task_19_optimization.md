# Task 19: Numerical Optimization

**Concept:** Optimization finds the inputs that minimise or maximise an objective function, often subject to constraints and bounds.

**Files:** [`code/Task_19_optimization.py`](../code/Task_19_optimization.py) (given program) · [`code/Task_19_extension.py`](../code/Task_19_extension.py) (parameter change + new real-world case)

---

## 1. Inputs and mathematical operation

- **Input values:** cost per unit (Type A = 12, Type B = 18), capacity per unit (A = 100, B = 170), required capacity ≥ 1000, bounds x, y ≥ 0, starting point (5, 3).
- **Mathematical operation:** minimise 12x + 18y subject to 100x + 170y − 1000 ≥ 0 with `minimize(..., method="SLSQP")`; then a brute-force search of whole-number combinations.

## 2. Output of the program

```text
Optimization success: True
Type A allocation: 0.000
Type B allocation: 5.882
Total capacity: 1000.00
Minimum planning cost: 105.88
Best nearby integer solution (cost, A, B, capacity): (108, 0, 6, 1020)
```

## 3. Interpretation of the output

The cheapest plan uses **no Type A and 5.882 units of Type B**, with total capacity exactly 1,000 (the constraint is active) at a cost of **105.88**. Type B is cheaper per unit of capacity (18/170 = 0.106 vs 12/100 = 0.12). Since whole servers are required, the best integer solution is **6 Type B servers (capacity 1,020, cost 108)**. There is no graph in this task.

## 4. Changing an input / parameter

**Change made:** the required capacity 1000 → **1500**, and then the Type B price 18 → **22**.

```text
capacity>=1000, cost A=12, B=18: A=0.000, B=5.882, cost=105.88
capacity>=1500, cost A=12, B=18: A=0.000, B=8.824, cost=158.82
capacity>=1000, cost A=12, B=22: A=10.000, B=0.000, cost=120.00
```

**How the result changes:** With 1,500 required the cost scales to 158.82 (all Type B, 8.82 units). Raising Type B's price to 22 makes it more expensive per unit capacity (0.129 vs 0.12), so the optimum *switches completely* to **10 Type A servers** at a cost of 120. A small price change can flip the best decision.

## 5. Modified program for a different but related real-world case

**Case:** Production planning: maximise profit

**New assumptions**

- A workshop makes chairs (profit 40 each) and tables (profit 30 each).
- Machine time: 2·chairs + tables ≤ 100 h. Labour: chairs + tables ≤ 80 h. Chair demand ≤ 40.
- Maximising profit is done by minimising its negative.

**Input data:** Constraints defined in `code/Task_19_extension.py`.

**Output**

```text
Chairs=20.00, Tables=60.00, Max profit=2600.00
Machine hours used: 100.00/100, labour hours used: 80.00/80
Integer check (best whole numbers): (2600, 20, 60)
```

**Interpretation:** The best plan is **20 chairs and 60 tables** for a profit of **2,600**. Both machine time (100/100) and labour (80/80) are fully used (binding constraints), and the chair demand limit is not. The whole-number check returns the same plan, so rounding is not needed.
