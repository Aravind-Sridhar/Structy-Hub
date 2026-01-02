# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

#Recursive
# def is_univalue_list(head):
#   if head is None:
#     return True
#   if head.next is None:
#     return True
#   if head.val != head.next.val:
#     return False
#   return is_univalue_list(head.next)

#Iterative
def is_univalue_list(head):
  if head is None:
    return True
  curr = head

  while curr:
    if curr.val != curr.next.val:
      return False
    curr = curr.next

  return True