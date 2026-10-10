class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#     a
#    / \
#   b   c
#  / \   \
# d   e   f

def depth_first_values(root):
  if not root:
    return []

  stack = [root]
  values = []

  while stack:
    node = stack.pop()
    values.append(node.val)
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)
  return values



def breadth_first_values(root):
  if not root:
    return []
  values = []
  queue = [ root ]
  while queue:
    current = queue.pop(0)
    values.append(current.val)

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
  return values



def max_path_sum(root):
  if root is None:
    return float('-inf')
  if root.left is None and root.right is None:
    return root.val

  max_left = max_path_sum(root.left)
  max_right = max_path_sum(root.right)

  return root.val + max(max_left, max_right)


def path_finder(root, target):
  if root is None:
    return None

  if root.val == target:
    return [ root.val ]

  left_path = path_finder(root.left, target)
  if left_path is not None:
    return [ root.val, *left_path ]

  right_path = path_finder(root.right, target)
  if right_path is not None:
    return [ root.val, *right_path ]

  return None

def tree_value_count(root, target):
  if root is None:
    return 0

  match = 1 if root.val == target else 0

  return match + tree_value_count(root.left, target) + tree_value_count(root.right, target)


def how_high(root):
  if root is None:
    return -1

  left_height = how_high(root.left)
  right_height = how_high(root.right)
  return 1 + max(left_height, right_height)


from collections import deque

def bottom_right_value(root):
  queue = deque([ root ])
  current = None

  while queue:
    current = queue.popleft()

    if current.left is not None:
      queue.append(current.left)

    if current.right is not None:
      queue.append(current.right)

  return current.val
