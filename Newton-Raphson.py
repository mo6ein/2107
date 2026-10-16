import math

def f(x):
    return x**2 - 2

def df(x):
    return 2*x

x = float(input("Enter initial guess: "))
tol = 1e-6
max_iter = 100

print("Iteration\t x\t\t f(x)")

for i in range(1, max_iter + 1):
    fx = f(x)
    dfx = df(x)

    if abs(dfx) < 1e-12:
        print("Derivative is zero.")
        break

    x_new = x - fx / dfx

    print(f"{i}\t\t {x_new:.8f}\t {f(x_new):.8f}")

    if abs(x_new - x) < tol:
        x = x_new
        print(f"\nApproximate root: {x:.8f}")
        break

    x = x_new
else:
    print("Method did not converge.")