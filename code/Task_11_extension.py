"""Task 11 extension: (A) change cash flows / start values, (B) loan interest rate."""
from scipy.optimize import root_scalar

def make(cf):
    npv = lambda r: sum(c / (1 + r)**t for t, c in enumerate(cf))
    dnpv = lambda r: sum(-t * c / (1 + r)**(t + 1) for t, c in enumerate(cf) if t)
    return npv, dnpv

print("=== PART A: change the initial investment and starting guess ===")
for invest, x0 in ((10000, 0.10), (12000, 0.10), (12000, 0.90)):
    npv, dnpv = make([-invest, 3000, 3500, 4000, 2500])
    try:
        s = root_scalar(npv, fprime=dnpv, x0=x0, method="newton", xtol=1e-12)
        print(f"investment={invest}, x0={x0}: IRR={s.root:.4%}, iterations={s.iterations}")
    except Exception as e:
        print(f"investment={invest}, x0={x0}: failed ({type(e).__name__})")

print("\n=== PART B: true monthly interest rate of an instalment loan ===")
# Assumption: borrow 5,000, repay 230 per month for 24 months. Find monthly rate i where
# 5000 = 230 * (1 - (1+i)^-24) / i
P, pmt, n = 5000.0, 230.0, 24
f = lambda i: pmt * (1 - (1 + i)**-n) / i - P
s = root_scalar(f, x0=0.005, x1=0.03, method="secant", xtol=1e-12)
print(f"Monthly rate (secant): {s.root:.4%} after {s.iterations} iterations")
print(f"Nominal annual rate  : {s.root*12:.2%}")
print(f"Effective annual rate: {(1+s.root)**12 - 1:.2%}")
print(f"Total repaid: {pmt*n:.0f}, interest paid: {pmt*n-P:.0f}")
