# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def path_finder(root, target):
  result = _path_finder(root, target)
  if result:
    return result[::-1]
  return None

def _path_finder(root, target):

  if not root:
    return None

  if root.val == target:
    return [root.val]

  left = _path_finder(root.left,target)
  if left:
    left.append(root.val)
    return left

  right = _path_finder(root.right, target)
  if right:
    right.append(root.val)
    return right

  return None

  