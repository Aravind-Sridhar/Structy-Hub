from math import floor, ceil
def is_prime(n):
  if n < 2:
    return False
  for i in range(2, floor(n**0.5)+1):
    if (n%i) == 0:
      return False
  return True