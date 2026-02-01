# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# Depth first iterative
# def tree_levels(root):

#   if not root:
#     return []

#   result = []

#   stack = [(root, 0)]

#   while stack:

#     node, level = stack.pop()

#     if len(result) == level:
#       result.append([node.val])
#     else:
#       result[level].append(node.val)
#     if node.right:
#       stack.append((node.right, level+1))
#     if node.left:
#       stack.append((node.left, level+1))

#   return result

# Breath first iterative
from collections import deque
def tree_levels(root):

  if not root:
    return []

  result = []

  queue = deque( [(root, 0)] )

  while queue:

    node, level = queue.popleft()

    if len(result) == level:
      result.append([node.val])
    else:
      result[level].append(node.val)

    if node.left:
      queue.append((node.left, level+1))
    if node.right:
      queue.append((node.right, level+1))

  return result


  