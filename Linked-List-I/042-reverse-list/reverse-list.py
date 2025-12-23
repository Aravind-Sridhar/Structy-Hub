# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# ------------- Iterative -----------------------------------

# def reverse_list(head):
#   current = head
#   prev = None

#   while current is not None:
#     next = current.next
#     current.next = prev
#     prev = current
#     current = next

#   return prev

# ----------------------------------------------------------

# ----------------------Recursive--------------------------- 

def reverse_list(head, prev = None):
  if head is None:
    return prev
  next = head.next
  head.next = prev

  return reverse_list(next, head)