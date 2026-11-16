# Task 16: Numerical Integration

**Concept:** An integral is accumulated quantity (area under a curve). The trapezoidal rule uses straight-line segments; Simpson's rule uses parabolas and is usually more accurate for smooth data.

**Files:** [`code/Task_16_numerical_integration.py`](../code/Task_16_numerical_integration.py) (given program) · [`code/Task_16_extension.py`](../code/Task_16_extension.py) (parameter change + new real-world case)

---

## 1. Inputs and mathematical operation

- **Input values:** power readings (0.8 to 1.8 kW) every 2 hours from 0 to 12 h.
- **Mathematical operation:** energy = ∫ P dt by the trapezoidal rule and by Simpson's rule.

## 2. Output of the program

```text
Energy using trapezoidal rule: 15.700 kWh
Energy using Simpson's rule:   15.800 kWh
Difference between estimates:  0.100 kWh
```

## 3. Interpretation of the output

The meter consumed about **15.7 kWh** (trapezoid) or **15.8 kWh** (Simpson) in 12 hours, an average of about 1.3 kW. The two methods differ by only 0.1 kWh, so the result is stable. Simpson's value is normally closer to the truth for smooth power curves. There is no graph in this task.

## 4. Changing an input / parameter

**Change made:** the sampling step was changed from 6 h to 3 h, 2 h and 1 h for a smooth known power curve whose exact energy is 18.98 kWh.

```text
Exact energy: 18.9837 kWh
step 6 h: trapezoid=18.0000 (err 0.9837), simpson=19.2000 (err 0.2163)
step 3 h: trapezoid=18.7456 (err 0.2381), simpson=18.9941 (err 0.0105)
step 2 h: trapezoid=18.8785 (err 0.1052), simpson=18.9856 (err 0.0020)
step 1 h: trapezoid=18.9575 (err 0.0262), simpson=18.9838 (err 0.0001)
```

**How the result changes:** Both estimates improve as the step shrinks, but Simpson's rule improves much faster: at 1 h the trapezoid error is 0.026 kWh, whereas Simpson's is only 0.0001 kWh. Halving the step reduces the trapezoid error about 4× and Simpson's about 16×.

## 5. Modified program for a different but related real-world case

**Case:** Total water volume passing a river gauge during a storm

**New assumptions**

- Discharge (m³/s) is logged every 30 min for 6 hours; flow before the storm is 12 m³/s.
- Volume = ∫ Q dt, with time converted to seconds.
- Data are illustrative.

**Input data:** `q` array (13 readings) in `code/Task_16_extension.py`.

**Output**

```text
Volume (trapezoid): 1,257,300 m^3 = 1.257 million m^3
Volume (Simpson)  : 1,261,800 m^3 = 1.262 million m^3
Peak flow 120 m^3/s at t=2.5 h; mean flow 58.4 m^3/s
Storm excess over base flow (12 m^3/s): 1.003 million m^3
```

**Interpretation:** About **1.26 million m³** of water passed during the 6 hours (trapezoid 1.257, Simpson 1.262 million m³). The peak was 120 m³/s at 2.5 h. Subtracting the normal flow leaves about **1.0 million m³** of storm water, which is useful for sizing flood-storage capacity. The two rules agree to within 0.4 %.
