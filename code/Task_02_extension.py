"""Task 2 extension: (A) parameter change, (B) new case - soil-moisture sensor grid."""
import numpy as np

print("=== PART A: change one input (heat-wave afternoon) ===")
base = np.array([18.5, 18.0, 17.8, 17.5, 17.9, 19.0, 21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
                 29.4, 29.1, 28.5, 27.6, 26.2, 24.8, 23.4, 22.1, 21.0, 20.2, 19.6, 19.0])
changed = base.copy()
changed[12] = 38.0          # one afternoon reading changed from 29.4 C to 38.0 C
for name, arr in (("Original", base), ("Changed ", changed)):
    print(f"{name}: mean={arr.mean():.2f} C, min={arr.min():.2f} C, max={arr.max():.2f} C")
print(f"Mean rose by {changed.mean() - base.mean():.2f} C; min unchanged; max rose by {changed.max() - base.max():.2f} C")

print("\n=== PART B: soil-moisture grid (2-D array) ===")
# Rows = 7 days, columns = 4 field sensors; values = volumetric water content (%)
moisture = np.array([
    [32.0, 30.5, 28.0, 35.0],
    [31.0, 29.8, 26.5, 34.1],
    [29.5, 28.0, 24.0, 33.0],
    [27.8, 26.9, 21.5, 31.7],
    [26.0, 25.5, 19.0, 30.2],
    [34.0, 33.5, 30.0, 36.0],   # irrigation / rain on day 6
    [32.5, 31.9, 28.7, 35.2],
])
threshold = 25.0            # assumed: crop stress below 25 %
print("Mean per sensor (%):", np.round(moisture.mean(axis=0), 2))
print("Minimum per sensor (%):", moisture.min(axis=0))
print("Days below threshold per sensor:", (moisture < threshold).sum(axis=0))
print("Sensor needing most attention: sensor", int(np.argmin(moisture.mean(axis=0))) + 1)
