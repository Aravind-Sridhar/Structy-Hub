from collections import Counter
def intersection(a, b):
  result = []
  dict_a = Counter(a)
  dict_b = Counter(b)

  for key, val in dict_a.items():
    if key in dict_b:
      result.append(key)

  return result
  