s = input()
s = s.lstrip('{').rstrip('}').split(', ')
seen = []
if s is not None:
    for i in s:
        if i not in seen:
            seen.append(i)
if seen[0] != '':
    print(len(seen))
else:
    print(0)