class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

#Iterative 
# def merge_lists(head_1, head_2):
#   dummy = Node(None)
#   tail = dummy
#   curr1 = head_1
#   curr2 = head_2

#   while curr1 and curr2:
#     if curr1.val < curr2.val:
#       tail.next = curr1
#       curr1 = curr1.next
#     else:
#       tail.next = curr2
#       curr2 = curr2.next
#     tail = tail.next

#   if not curr1:
#     tail.next = curr2
#   if not curr2:
#     tail.next = curr1

#   return dummy.next

#Recursive
def merge_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None

  if head_1 is None:
    return head_2
  if head_2 is None:
    return head_1

  if head_1.val < head_2.val:
    next_1 = head_1.next
    head_1.next = merge_lists(next_1, head_2)
    return head_1
  else:
    next_2 = head_2.next
    head_2.next = merge_lists(head_1, next_2)
    return head_2
