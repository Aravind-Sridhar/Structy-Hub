# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root, min_val = float('inf')):
  if not root:
    return min_val

  if root.val < min_val:
    min_val = root.val

  min_right = tree_min_value(root.right, min_val)
  min_left = tree_min_value(root.left, min_val)

  return min(min_right, min_left)

  