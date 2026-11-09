# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def longest_streak(head):
  longest = 0
  curr = 0
  prev = None

  current = head
  while current:
    if current.val == prev:
      curr+=1
    else:
      curr=1

    if curr>longest:
      longest = curr
    prev = current.val
    current = current.next


  return longest
