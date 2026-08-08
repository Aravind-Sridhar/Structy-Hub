def has_substring_anagram(s, anagram):
  comp = set(anagram)
  k = len(anagram)

  curr = set(s[0:k])
  if curr == comp:
    return True

  for i in range(len(s)-k):
    curr.remove(s[i])
    curr.add(s[i+k])

    if curr_comp == comp:
      return True

  return False