# Task 2: NumPy Arrays and Numerical Computation

**Concept:** An array is an ordered collection of numbers; NumPy applies one operation to every element without an explicit loop.

**Files:** [`code/Task_02_numpy_arrays.py`](../code/Task_02_numpy_arrays.py) (given program) · [`code/Task_02_extension.py`](../code/Task_02_extension.py) (parameter change + new real-world case)

---

## 1. Inputs and mathematical operation

- **Input values:** a 1-D array of 24 hourly temperatures in °C (17.5 °C to 29.4 °C).
- **Mathematical operations:** mean = (Σ xᵢ)/n, minimum, maximum, and the element-wise conversion **F = 1.8·C + 32** applied to the whole array at once.

## 2. Output of the program

```text
Daily mean temperature: 23.12 C
Minimum temperature: 17.50 C
Maximum temperature: 29.40 C
First six Fahrenheit readings: [65.3  64.4  64.04 63.5  64.22 66.2 ]
```

## 3. Interpretation of the output

- The **mean (23.12 °C)** is the typical temperature of the day; the **minimum (17.50 °C)** occurs in the early hours (03:00) and the **maximum (29.40 °C)** at midday (12:00), so the daily range is 11.9 °C.
- The Fahrenheit values (65.3 °F, 64.4 °F, ...) are the same readings in a different unit: the whole array was converted in one expression, `1.8 * temperatures_c + 32`.
- There is no graph in this task.

## 4. Changing an input / parameter

**Change made:** the 12:00 reading was changed from 29.4 °C to **38.0 °C** (a heat-spike / faulty sensor).

```text
Original: mean=23.12 C, min=17.50 C, max=29.40 C
Changed : mean=23.48 C, min=17.50 C, max=38.00 C
Mean rose by 0.36 C; min unchanged; max rose by 8.60 C
```

**How the result changes:** The **maximum** rose by exactly 8.6 °C because the changed value *is* the new maximum, the **minimum** stayed the same because that reading was not touched, and the **mean** rose by 0.36 °C (= 8.6 / 24). The mean reacts to every value but each value only carries a weight of 1/24, whereas the max reacts completely to one extreme value. This shows why one faulty IoT reading can distort a maximum but only slightly moves an average.

## 5. Modified program for a different but related real-world case

**Case:** Soil-moisture monitoring for a farm (IoT sensor grid)

**New assumptions**

- 4 sensors are buried in different parts of a field and report once per day for 7 days (a 7 × 4 **2-D array**).
- Values are volumetric water content in %. Crops are assumed to be stressed below **25 %**.
- Irrigation/rain occurs on day 6.

**Input data:** `moisture` array in `code/Task_02_extension.py` (7 rows = days, 4 columns = sensors).

**Output**

```text
Mean per sensor (%): [30.4  29.44 25.39 33.6 ]
Minimum per sensor (%): [26.  25.5 19.  30.2]
Days below threshold per sensor: [0 0 3 0]
Sensor needing most attention: sensor 3
```

**Interpretation:** Using `axis=0` NumPy computes statistics **per sensor** across all days in one call. Sensor 3 has the lowest mean (25.39 %), its minimum falls to 19 %, and it is the only sensor below the 25 % threshold, on **3 of the 7 days**. This area of the field dries fastest and should be irrigated first or have its drainage checked. The other three sensors stay above the threshold throughout.
