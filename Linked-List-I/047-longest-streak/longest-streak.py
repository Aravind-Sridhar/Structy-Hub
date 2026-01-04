# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def longest_streak(head):
  if not head:
    return 0
  max_streak = 0
  curr_streak = 0
  prev_val = head.val
  curr = head

  while curr:
    if prev_val == curr.val:
      curr_streak+=1
    else:
        curr_streak = 1
    max_streak = max(max_streak, curr_streak)
    prev_val = curr.val
    curr = curr.next

  return max_streak
      