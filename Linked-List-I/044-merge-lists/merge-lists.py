class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

#Iterative 
def merge_lists(head_1, head_2):
  dummy = Node(None)
  tail = dummy
  curr1 = head_1
  curr2 = head_2

  while curr1 and curr2:
    if curr1.val < curr2.val:
      tail.next = curr1
      curr1 = curr1.next
    else:
      tail.next = curr2
      curr2 = curr2.next
    tail = tail.next

  if not curr1:
    tail.next = curr2
  if not curr2:
    tail.next = curr1

  return dummy.next
