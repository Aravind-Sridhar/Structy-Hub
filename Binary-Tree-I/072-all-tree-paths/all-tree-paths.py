# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def all_tree_paths(root):
  paths = _all_tree_paths(root)

  for path in paths:
    path.reverse()
  return paths

def _all_tree_paths(root):
  if not root:
    return []

  if root.left is None and root.right is None:
    return [[root.val]]
  
  all_path = []
  left = _all_tree_paths(root.left)
  for path in left:
    path.append(root.val)
    all_path.append(path)
  right = _all_tree_paths(root.right)
  for path in right:
    path.append(root.val)
    all_path.append(path)

  return all_path