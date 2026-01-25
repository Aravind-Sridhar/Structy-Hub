# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def how_high(root):
  if not root:
    return 1

  left_depth = how_high(root.left)
  right_depth = how_high(root.right)

  return 1 + max(left_depth, right_depth)
