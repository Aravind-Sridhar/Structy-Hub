# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):
  if not root:
    return []

  stack = [root]
  result = []

  while stack:
    current = stack.pop()
    result.append(current.val)
    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)

  return result