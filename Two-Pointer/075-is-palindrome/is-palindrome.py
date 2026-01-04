#Recursive
# def is_palindrome(s):
#   if len(s) <= 1:
#     return True
#   if s[0] != s[-1]:
#     return False
#   return is_palindrome(s[1:-1])

#Two pointer
def is_palindrome(s):
  l,r = 0, len(s)-1

  while l < r:
    if s[l] != s[r]:
      return False
    l+=1
    r-=1

  return True