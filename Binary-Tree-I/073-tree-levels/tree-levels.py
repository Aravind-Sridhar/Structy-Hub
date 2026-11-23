from collections import deque
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_levels(root):
  if not root:
    return []

  levels = []
  queue = deque([(root, 0)])
  while queue:
    vals, level = queue.popleft()
    if len(levels) == level:
      levels.append([vals.val])
    else:
      levels[level].append(vals.val)
    if vals.left:
      queue.append((vals.left, level +1))
    if vals.right:
      queue.append((vals.right, level +1))
  return levels
  