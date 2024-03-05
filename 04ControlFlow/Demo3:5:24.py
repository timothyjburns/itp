def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n - 1)

n = 3

print(f"Factorial of {n} is {factorial(n)}")
