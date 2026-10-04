def counter(n):
    if n == 0:
        return
    print(n)
    counter(n - 1)

counter(5)

def sum_numbers_recursive(numbers):
  if len(numbers) == 0:
    return 0
  return numbers[0] + sum_numbers_recursive(numbers[1:])


def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n - 1)

def sum_of_lengths(strings):
  if len(strings) == 0:
    return 0
  return len(strings[0]) + sum_of_lengths(strings[1:])

def reverse_string(s):
  if len(s) == 0:
    return ''
  return reverse_string(s[1:]) + s[0]


def palindrome(s):
  if len(s) <=1:
    return True

  if s[0] != s[-1]:
    return False

  return palindrome(s[1:-1])


def fibonacci(n):
    if n == 0 or n == 1:
      return n
    return fibonacci(n - 1) + fibonacci(n - 2)
