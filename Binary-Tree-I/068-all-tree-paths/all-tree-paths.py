# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def all_tree_paths(root):
  result = _all_tree_paths(root)

  for res in result:
    res.reverse()

  return result

def _all_tree_paths(root):
  if not root:
    return []

  if root.left is None and root.right is None:
    return [[root.val]]

  result = []

  left_paths = _all_tree_paths(root.left)

  for paths in left_paths:
    paths.append(root.val)
    result.append(paths)

  right_paths = _all_tree_paths(root.right)

  for paths in right_paths:
    paths.append(root.val)
    result.append(paths)

  return result