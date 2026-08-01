from collections import Counter
def intersection_with_dupes(a, b):
  dic1 = Counter(a)
  dic2 = Counter(b)
  result = []

  for char in dic1:
    if char in dic2:
      count = min(dic1[char], dic2[char])
      result.extend([char]*count)

  return result