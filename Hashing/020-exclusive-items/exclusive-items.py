from collections import Counter
def exclusive_items(a, b):
  result = []
  dict_a = Counter(a)
  dict_b = Counter(b)
  for key, val in dict_a.items():
    if key not in dict_b:
      result.append(key)
    del dict_b[key]

  for x in dict_b.keys():
    result.append(x)
  
  return result