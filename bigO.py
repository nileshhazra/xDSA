print('big O notation!')
def fizz_buzz(n):
  arr = []
  for i in range(1,n + 1):
    if i % 3 == 0 and i % 5 == 0:
      arr.append('fizzbuzz')
    elif i % 5 == 0:
      arr.append('buzz')
    elif i % 3 == 0:
      arr.append('fizz')
    else:
      arr.append(i)
  return arr

print(fizz_buzz(16))


def pairs(elements):
    result = []

    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            pair = [elements[i], elements[j]]
            result.append(pair)

    return result


print(pairs(['a', 'b', 'c', 'd']))
