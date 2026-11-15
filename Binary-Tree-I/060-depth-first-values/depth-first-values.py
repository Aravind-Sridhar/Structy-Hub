# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):

  #Recursive 
  if not root:
    return []

  left = depth_first_values(root.left)
  right = depth_first_values(root.right)

  return [root.val, *left, *right]

  # ## Iterative
  # if not root:
  #   return []

  # stack = [root]
  # res = []

  # while root:
  #   val = stack.pop()
  #   res.append(val.val)

  #   if val.right:
  #     stack.append(val)
  #   if val.left:
  #     stack.append(val)

  #   return res
    
