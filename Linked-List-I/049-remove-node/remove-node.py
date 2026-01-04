# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def remove_node(head, target_val):
  if target_val == head.val:
    return head.next

  curr = head
  prev = None

  while curr:
    if curr.val != target_val:
      prev = curr
      curr = curr.next
    else:
      prev.next = curr.next
      break

  return head
