class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):
  ins_val = Node(value)
  if index == 0:
    ins_val.next = head
    return ins_val

  current = head
  prev = None
  while current:
    if index == 0:
      ins_val.next = current
      prev.next = ins_val
      return head
      
    index-=1
    prev = current
    current = current.next
  if index
  return head
