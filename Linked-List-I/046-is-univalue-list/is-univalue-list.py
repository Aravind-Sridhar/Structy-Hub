# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

#Recursive
def is_univalue_list(head):
  if head is None:
    return True
  if head.next is None:
    return True
  if head.val != head.next.val:
    return False
  return is_univalue_list(head.next)
