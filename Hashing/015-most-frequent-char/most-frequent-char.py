from collections import Counter

def most_frequent_char(s):
  dict_s = Counter(s)
  char = ''
  max_val = -float('inf')

  for key, val in dict_s.items():
    if val > max_val:
      max_val = val
      char = key

  return char