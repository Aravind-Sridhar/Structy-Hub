#Approch 1 - build a dict and check max value
from collections import Counter
def most_frequent_char(s):
  dic = Counter(s)
  max_val = -1
  result = ''

  for key, val in dic.items():
    if val > max_val:
      result = key
      max_val = val

  return result
      