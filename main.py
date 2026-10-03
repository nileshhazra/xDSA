print('daily python!')

def majority_element(nums: list[int]) -> int:
    majority = len(nums) / 2
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 0
        count[num] += 1
        if count[num] > majority:
            return num
    return -1

from collections import Counter


def majority_element_p(nums: list[int]) -> int:
    majority = len(nums) / 2
    count = Counter(nums)
    for ele in count:
        if count[ele] > majority:
            return ele
    return -1

print(majority_element([3, 2, 3]))
print(majority_element([2, 2, 1, 1, 1, 2, 2]))
print(majority_element_p([2, 2, 1, 1, 1, 2, 2]))

