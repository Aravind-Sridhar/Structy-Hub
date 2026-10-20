# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_find(head, target):
  if not head:
    return False

  if head.val == target:
    return True

  return linked_list_find(head.next, target)
