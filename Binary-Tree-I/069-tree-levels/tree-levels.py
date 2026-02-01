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
# from collections import deque
# def tree_levels(root):

#   if not root:
#     return []

#   result = []

#   queue = deque( [(root, 0)] )

#   while queue:

#     node, level = queue.popleft()

#     if len(result) == level:
#       result.append([node.val])
#     else:
#       result[level].append(node.val)

#     if node.left:
#       queue.append((node.left, level+1))
#     if node.right:
#       queue.append((node.right, level+1))

#   return result

## Breath first recursive

def tree_levels(root):
  result = []
  _tree_levels(root, result, 0)
  return result
  

def _tree_levels(node, result, level_num):
  if not node:
    return

  if level_num == len(result):
    result.append([node.val])
  else:
    result[level_num].append(node.val)

  _tree_levels(node.left, result, level_num+1)
  _tree_levels(node.right, result, level_num+1)
