"""Task 3 extension: (A) change N, (B) solar panel output over a year (8,760 hours)."""
import numpy as np, timeit

print("=== PART A: change the number of readings ===")
rng = np.random.default_rng(42)
for n in (10_000, 1_000_000, 5_000_000):
    data = rng.uniform(5, 250, n)
    def loop():
        return [(v / 1000.0) ** 2 for v in data]
    def vec():
        return (data / 1000.0) ** 2
    tl = timeit.timeit(loop, number=1)
    tv = timeit.timeit(vec, number=3) / 3
    print(f"N={n:>9,}: loop={tl:.4f} s, vectorized={tv:.5f} s, speed-up={tl/tv:.0f}x")

print("\n=== PART B: solar panel yield for every hour of a year ===")
# Assumptions: 20 m^2 array, 18 % efficiency, power falls 0.4 % per degree C above 25 C
hours = np.arange(8760)
hour_of_day = hours % 24
irradiance = np.clip(1000 * np.sin(np.pi * (hour_of_day - 6) / 12), 0, None)   # W/m^2
rng = np.random.default_rng(1)
cloud = rng.uniform(0.4, 1.0, hours.size)                                       # cloud factor
cell_temp = 22 + 0.03 * irradiance                                              # C
power_w = 20 * 0.18 * irradiance * cloud * (1 - 0.004 * (cell_temp - 25).clip(0))
energy_kwh = power_w.sum() / 1000                                               # 1 h steps
print(f"Peak power: {power_w.max():.0f} W")
print(f"Average daily energy: {energy_kwh / 365:.2f} kWh")
print(f"Annual energy: {energy_kwh:.0f} kWh")
print(f"Annual savings at 0.18 USD/kWh: {energy_kwh * 0.18:.0f} USD")
