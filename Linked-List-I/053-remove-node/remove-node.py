# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def remove_node(head, target_val):
  if target_val == head.val:
    return head.next

  current = head
  prev = None
  while current:
    if current.val == target_val:
      prev.next = current.next
      break
    prev = current
    current = current.next

  return head
