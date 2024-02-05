first = input()
second = input()
result = []
for i, j in zip(first, second):
    if i == j:
        result.append('0')
    else:
        result.append('1')
result = ''.join(result)
print(result)