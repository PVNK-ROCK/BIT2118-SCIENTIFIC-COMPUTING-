# Task 3: Mathematical Functions and Vectorization

**Concept:** Vectorization applies a mathematical function to all elements of an array in one expression, using fast compiled code instead of a Python loop.

**Files:** [`code/Task_03_vectorization.py`](../code/Task_03_vectorization.py) (given program) · [`code/Task_03_extension.py`](../code/Task_03_extension.py) (parameter change + new real-world case)

---

## 1. Inputs and mathematical operation

- **Input values:** 1,000,000 simulated latency readings (uniform random between 5 and 250 ms, seed 42).
- **Mathematical operations:** conversion ms → s (divide by 1000) and squaring, (v/1000)². Done once in a Python loop and once as a vectorized expression; `timeit` measures both.

## 2. Output of the program

```text
First five squared latency values: [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
Loop time: 0.1397 s
Vectorized time: 0.0028 s
Approximate speed-up: 50.0x
```

## 3. Interpretation of the output

- The first five squared values (about 0.0008 to 0.046 s²) are the squared latencies in seconds. Both versions compute exactly the same numbers.
- The vectorized version ran in a few milliseconds while the loop took over a tenth of a second, a speed-up of about **50×**. Exact timings differ from computer to computer, but the vectorized version is always much faster.
- There is no graph in this task.

## 4. Changing an input / parameter

**Change made:** the number of readings *N* was changed to 10,000, 1,000,000 and 5,000,000.

```text
N=   10,000: loop=0.0016 s, vectorized=0.00003 s, speed-up=59x
N=1,000,000: loop=0.1418 s, vectorized=0.00222 s, speed-up=64x
N=5,000,000: loop=0.7364 s, vectorized=0.00842 s, speed-up=87x
```

**How the result changes:** The speed-up grew from about 59× to 87× as N increased. A Python loop pays interpreter overhead on every single element, while NumPy pays a small fixed start-up cost once and then runs a tight compiled loop. The larger the data, the more the fixed cost is spread out and the bigger the advantage. (Timings vary between runs.)

## 5. Modified program for a different but related real-world case

**Case:** Annual energy yield of a rooftop solar panel (8,760 hourly values)

**New assumptions**

- Panel area 20 m², efficiency 18 %.
- Power falls by 0.4 % for every °C the cell is above 25 °C; cell temperature = 22 + 0.03 × irradiance.
- Irradiance follows a half-sine from 06:00 to 18:00 with a 1000 W/m² peak, multiplied by a random cloud factor between 0.4 and 1.0.
- Electricity is valued at 0.18 USD/kWh (an assumed tariff).

**Input data:** Generated inside `code/Task_03_extension.py` with `np.arange(8760)` and a seeded random generator.

**Output**

```text
Peak power: 3210 W
Average daily energy: 17.53 kWh
Annual energy: 6399 kWh
Annual savings at 0.18 USD/kWh: 1152 USD
```

**Interpretation:** A whole year of hourly calculations (8,760 values, several formulas each) is done with array expressions and no loops. The peak power of **3,210 W** is below the ideal 3,600 W (20 × 0.18 × 1000) because of the heat penalty. The panel produces about **17.5 kWh/day**, **≈ 6,400 kWh/year**, worth roughly **1,150 USD** at the assumed tariff. Night-time hours give 0 W automatically because negative irradiance was clipped to 0.
