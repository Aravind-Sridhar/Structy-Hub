# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

#Iterative
# def depth_first_values(root):
#   if not root:
#     return []

#   stack = [root]
#   result = []

#   while stack:
#     current = stack.pop()
#     result.append(current.val)
#     if current.right:
#       stack.append(current.right)
#     if current.left:
#       stack.append(current.left)

#   return result

def depth_first_values(root):
  if not root:
    return []

  left_val = depth_first_values(root.left)
  right_val = depth_first_values(root.right)

  return [root.val, *left_val, *right_val]