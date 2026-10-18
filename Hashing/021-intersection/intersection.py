from collections import Counter
def intersection(a, b):
  res = []

  dic_a = Counter(a)
  dic_b = Counter(b)

  for x in dic_a:
    if x in Counter(b):
      res.append(x)

  return res
  