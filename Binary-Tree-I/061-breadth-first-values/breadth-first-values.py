from collections import deque
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def breadth_first_values(root):
  if not root:
    return []

  queue = deque([root])
  res = []

  while queue:
    current = queue.popleft()
    res.append(current.val)

    if current.left:
      queue.app

  return res