class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d

def print_list(head):
  curr = head
  while curr is not None:
    print(curr.val)
    curr = curr.next

print_list(a)


def print_list_rec(head):
  if head is None:
    return
  print(head.val)
  print_list_rec(head.next)

print_list_rec(a)

def linked_list_values(head):
  res = []
  curr = head

  while curr is not None:
    res.append(curr.val)
    curr = curr.next

  return res

def linked_list_values_interative(head):
  values = []
  _linked_list_values(head, values)
  return values

def _linked_list_values(head, values):
  if head is None:
    return
  values.append(head.val)
  _linked_list_values(head.next, values)


def sum_list_i(head):
  curr = head
  sum = 0
  while curr is not None:
    sum += curr.val
    curr = curr.next
  return sum

def sum_list(head):
  if head is None:
    return 0
  return head.val + sum_list(head.next)

def linked_list_find(head, target):
  curr = head
  while curr is not None:
    if curr.val == target:
      return True
    curr = curr.next
  return False


def linked_list_find_r(head, target):
  if head is None:
    return False
  if head.val == target:
    return True
  return linked_list_find(head.next, target)


def get_node_value(head, index):
  curr = head
  idx = 0
  while curr is not None:
    if idx == index:
      return curr.val
    curr = curr.next
    idx += 1

  return None


def get_node_value_r(head, index):
  if head is None:
    return None
  if index == 0:
    return head.val

  return get_node_value(head.next, index - 1)



def reverse_list(head):
  prev = None
  curr = head
  while curr is not None:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  return prev

def reverse_list_recursive(head, prev = None):
  if head is None:
    return prev
  next = head.next
  head.next = prev
  return reverse_list(next, head)




def zipper_lists(head_1, head_2):
  tail = head_1
  current_1 = head_1.next
  current_2 = head_2
  count = 0
  while current_1 is not None and current_2 is not None:
    if count % 2 == 0:
      tail.next = current_2
      current_2 = current_2.next
    else:
      tail.next = current_1
      current_1 = current_1.next
    tail = tail.next
    count += 1


  if current_1 is not None:
    tail.next = current_1

  if current_2 is not None:
    tail.next = current_2

  return head_1


def zipper_lists_recursive(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None
  if head_1 is None:
    return head_2
  if head_2 is None:
    return head_1

  next_1 = head_1.next
  next_2 = head_2.next
  head_1.next = head_2
  head_2.next = zipper_lists(next_1, next_2)
  return head_1
