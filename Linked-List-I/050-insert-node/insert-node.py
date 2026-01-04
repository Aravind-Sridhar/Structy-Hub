class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):

  new = Node(value)
  
  if index == 0:
    new.next = head
    return new

  prev = None
  curr = head
  point = 0

  while curr:
    if point != index:
      point+=1
      prev = curr
      curr = curr.next
    else:
      prev.next = new
      new.next = curr
      break
  
  return head
