class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists(head_1, head_2):
  dummy_head = Node(None)
  tail = dummy_head
  current_1 = head_1
  current_2 = head_2

  while current_1 is not None and current_2 is not None:
    if current_1.val < current_2.val:
      tail.next = current_1
      current_1 = current_1.next
    else:
      tail.next = current_2
      current_2 = current_2.next
    tail = tail.next

  if current_1 is not None:
    tail.next = current_1
  if current_2 is not None:
    tail.next = current_2

  return dummy_head.next

def merge_lists_recursive(head_1, head_2):
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

def is_univalue_list(head):
  current = head
  while current is not None:
    if current.val != head.val:
      return False
    current = current.next
  return True

def is_univalue_list_r(head, prev_val = None):
  if head is None:
    return True
  if prev_val is None or head.val == prev_val:
    return is_univalue_list(head.next, head.val)
  else:
    return False



def longest_streak(head):
  max_streak = 0
  current_streak = 0
  prev_val = None

  current = head
  while current is not None:
    if current.val == prev_val:
      current_streak += 1
    else:
      current_streak = 1

    prev_val = current.val
    if current_streak > max_streak:
      max_streak = current_streak

    current = current.next

  return max_streak



def remove_node(head, target_val):
  current = head
  prev = None

  if head.val == target_val:
    return head.next

  while current is not None:
    if current.val == target_val:
      prev.next = current.next
      break

    prev = current
    current = current.next

  return head


def remove_node_r(head, target_val):
  if head is None:
    return None

  if head.val == target_val:
    return head.next

  head.next = remove_node(head.next, target_val)
  return head
