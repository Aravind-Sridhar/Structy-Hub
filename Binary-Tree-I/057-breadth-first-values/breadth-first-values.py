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
  result = []

  while queue:
    current = queue.popleft()

    result.append(current.val)

    if current.right:
      queue.append(current.right)
    if current.left:
      queue.append(current.left)

  return result
    

  
