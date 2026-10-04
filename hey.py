def maximum(arr):
    max = float('-inf')
    for ele in arr:
        if ele > max:  # noqa: PLR1730
            max = ele
    return max

print(maximum([5, 4, 9, 2, 1]))

def longest_word(str):
    longest = ''
    words = str.split()
    for word in words:
        if len(word) >= len(longest):
            longest = word
    return longest

print(longest_word('prevention is better than cure'))

def all_even(nums):
    for num in nums:
        if num % 2 != 0:
            return False
    return True

print(all_even([2, 4, 6, 8]))
print(all_even([1, 2, 3, 4]))
print(all_even([]))

from math import floor, sqrt


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, floor(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

print('is prime: ')
print(is_prime(3))
print(is_prime(5))
print(is_prime(6))
print(is_prime(35))
print(is_prime(53))
