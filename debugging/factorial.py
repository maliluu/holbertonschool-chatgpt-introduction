def factorial(n):
  result = 1
  while n >= 0:  # check if n is non-negative
    result *= n
    n -= 1
  return result
