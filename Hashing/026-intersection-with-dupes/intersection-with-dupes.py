from collections import Counter
def intersection_with_dupes(a, b):
  dic_a = Counter(a)
  dic_b = Counter(b)

  for key in dic_a:
    for i in range(0, min(dic_a[key], dic_b[key])):
      