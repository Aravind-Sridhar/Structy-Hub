from collections import Counter

def most_frequent_char(s):
  dict = Counter(s)
  dict = dict.most_common()

  return dict[0]
  