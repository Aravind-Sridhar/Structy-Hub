# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def get_node_value(head, index):
  if index == 0 and head is not None:
    return head.val

  return get_node_value(head.next,index-1)