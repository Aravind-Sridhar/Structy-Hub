# #Using sorting
# def count_substring_anagrams(s, anagram):
#   count = 0
#   k = len(anagram)
#   comp = sorted(anagram)

#   current = s[0:k]

#   if sorted(current) == comp:
#     count +=1

#   for i in range(len(s)-k):
#     current = current.replace(s[i], "", 1)
#     current+=s[i+k]

#     if sorted(current) == comp:
#       count+=1
#   return count
from collections import Counter
def count_substring_anagrams(s, anagram):
  k = len(anagram)
  comp = Counter(anagram)
  count = 0

  current = Counter(s[0:k])

  if current == comp:
    count+=1

  for i in range(len(s)-k):
    current[s[i]]-=1
    current[s[i+k]] +=1

    if current == comp:
      count+=1
    




  return count
  