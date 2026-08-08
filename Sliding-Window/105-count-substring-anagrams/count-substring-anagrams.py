def count_substring_anagrams(s, anagram):
  count = 0
  k = len(anagram)
  comp = sorted(anagram)

  current = s[0:k]

  if sorted(current) == comp:
    count +=1

  for i in range(len(s)-k):
    current = current.replace(s[i], "")
    current+=s[i+k]

    if sorted(current) == comp:
      count+=1
  return count