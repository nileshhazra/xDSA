def pair_sum(numbers, target_sum):
    previous_nums = {}

    for index, num in enumerate(numbers):
        compliment = target_sum - num
        if compliment in previous_nums:
            return (index, previous_nums[compliment])
        previous_nums[num] = index



print(pair_sum([2, 3, 4, 5], 7))

def pair_product(numbers, target_product):
    previous_nums = {}

    for index, num in enumerate(numbers):
        compliment = target_product / num
        if compliment in previous_nums:
            return (previous_nums[compliment], index)
        previous_nums[num] = index

print(pair_product([1, 2, 3, 4], 8))



def intersection_bf(a, b):
  res = []
  for i in range(0, len(a)):
    for j in range(0, len(b)):
      if a[i] == b[j]:
        res.append(a[i])
  return res


print(intersection_bf([4, 2, 1, 6], [3, 6, 9, 2, 10]))


def intersection(a, b):
#     result = []
#
#     for item in a:
#         if item in b:
#             result.append(item)
#
#     return result
    items_set = set()
    result = []

    for item in a:
        items_set.add(item)

    for ele in b:
        if ele in items_set:
                result.append(ele)

    return result


print(intersection([4, 2, 1, 6], [3, 6, 9, 2, 10]))


def intersection_python(a, b):
    items_set = set(a)
    return [ ele for ele in b if ele in items_set]

print(intersection_python([4, 2, 1, 6, 9, 7], [3, 6, 9, 2, 10]))




from collections import Counter


def intersection_with_dupes(a, b):
  count_a = Counter(a)
  count_b = Counter(b)
  result = []

  for ele in count_a:
    for i in range(0, min(count_a[ele], count_b[ele])):
      result.append(ele)

  return result

from collections import Counter


def intersection_with_dupes_me(a, b):
  result = []
  count_a = Counter(a)
  count_b = Counter(b)

  for ele in count_a:
    if ele in count_b:
      itr = min(count_a[ele], count_b[ele])
      for i in range(itr):
        result.append(ele)

  return result
