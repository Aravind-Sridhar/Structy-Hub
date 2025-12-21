from collections import Counter

def intersection_with_dupes(a, b):
  # dict_a = Counter(a)
  dict_b = Counter(b)
  result =[]

  for key in a:
      if key in dict_b and dict_b[key]>0:
          result.append(key)
          dict_b[key]-=1
    
  return result