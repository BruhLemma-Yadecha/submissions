length = int(input())
s = list(input().capitalize())
letters = []
for c in s:
    if c not in letters:
        letters.append(c)
if len(letters) >= 26:
    print("YES")
else:
    print(len(letters))
    print("NO")
