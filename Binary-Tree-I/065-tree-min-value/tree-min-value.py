from collections import deque
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):
  # if not root:
  #   return float('inf')
  # left = tree_min_value(root.left)
  # right = tree_min_value(root.right)

  # return min(root.val,left,right)

  queue = deque([root])
  small = float('inf')
  while queue:
    curr = queue.popleft()
    if curr.val < small:
      small = curr.val
    if curr.left:
      queue.append(curr.left)
    if curr.right:
      queue.append(curr.right)

  return small