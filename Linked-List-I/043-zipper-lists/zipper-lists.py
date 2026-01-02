# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def zipper_lists(head_1, head_2):
  tail = head_1
  curr1 = head_1.next
  curr2 = head_2
  n = 0

  while curr1 and curr2:
    if n % 2 == 0:
      tail.next = curr2
      curr2 = curr2.next
    else:
      tail.next = curr1
      curr1 = curr1.next
    n+=1
    tail = tail.next

  if curr1 is None:
    tail.next = curr2
  if curr2 is None:
    tail.next = curr1

  return head_1
