"""Task 4 extension: (A) change inputs, (B) accumulated round-off in a ledger."""
import numpy as np, math
from decimal import Decimal

print("=== PART A: change the approximation and the x values ===")
for approx in (1.414, 1.4142, 1.41421):
    ae = abs(np.sqrt(2) - approx)
    print(f"approx={approx}: absolute error={ae:.8f}, relative error={ae/np.sqrt(2):.6%}")
for x in (1e-14, 1e-16):
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)
    print(f"x={x:.0e}: direct={direct:.6f}, stable={stable:.6f}")

print("\n=== PART B: transaction-fee ledger (1,000,000 fees of 0.10) ===")
fee, n = 0.10, 1_000_000
naive = 0.0
for _ in range(n):
    naive += fee
accurate = math.fsum([fee] * n)
exact = Decimal("0.10") * n
print(f"Naive float sum   : {naive:.10f}")
print(f"math.fsum         : {accurate:.10f}")
print(f"Decimal (exact)   : {exact}")
print(f"Naive error       : {abs(naive - 100000):.3e}")
print("naive == 100000 ?", naive == 100000, "| np.isclose ?", np.isclose(naive, 100000))
