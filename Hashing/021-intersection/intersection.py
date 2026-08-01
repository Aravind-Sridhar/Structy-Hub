def intersection(a, b):
  s1 = set(a)
  s2 = set(b)
  result = []

  for num in s1:
    if num in s2:
      result.append(num)

  return result