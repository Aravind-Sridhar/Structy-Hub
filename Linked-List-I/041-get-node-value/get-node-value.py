# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def get_node_value(head, index):
  current = head
  if index == 0:
    return head.val
  idx = 0

  while current is not None:
    if idx == index:
      return current.val

    idx +=1
    current = current.next
