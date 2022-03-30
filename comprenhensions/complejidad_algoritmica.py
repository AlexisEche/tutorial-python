def factorial_r(n):
  if n == 1 :
    return 1

  return n * factorial_r(n-1)


print(factorial_r(5))