from collections import Counter
def exclusive_items(a, b):
  dic_a = Counter(a)
  dic_b = Counter(b)
  res= []
  for num in dic_a.keys():
    if num not in dic_b.keys():
      res.append(num)

  for num in dic_b.keys():
    if num not in dic_a.keys():
      res.append(num)
  return res