# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def path_finder(root, target):
  res = _path_finder(root,target)
  if not res:
    return None
  else:
    return res[::-1]


def _path_finder(root, target):
  if not root:
    return None
  if root.val == target:
    return [root.val]

  left = _path_finder(root.left,target)
  right = _path_finder(root.right, target)
  if left:
    left.append(root.val)
    return left
  if right:
    right.append(root.val)
    return right
  return None
  
