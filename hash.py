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


def most_frequent_char(s):
    count = Counter(s)

    res = None

    for char in s:
        if res is None or count[char] > count[res]:
            res = char

    return res

print(most_frequent_char('skepticisms'))
