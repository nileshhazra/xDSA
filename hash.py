def anagramsf(s1, s2):
    def char_count(s):
        count = {}
        for char in s:
            if char not in count:
                count[char] = 0
            count[char] += 1
        return count

    return char_count(s1) == char_count(s2)


print(anagramsf('abcd', 'dbac'))




# using python collections library

from collections import Counter


def anagrams(s1, s2):
    return Counter(s1) == Counter(s2)


print(anagrams('car','ract'))
