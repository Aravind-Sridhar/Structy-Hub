# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_values(head):
  # res = []
  # current = head

  # while current:
  #   res.append(current.val)
  #   current = current.next

  # return res

  res = []
  _linked_list_values(head, res)

  return res

  # Recursive

def _linked_list_values(head, lis):
  if not head:
    return
  lis.append(head.val)
  _linked_list_values(head.next, lis)