line = input()
line = input().split(' ')

easy = True
for i in line:
    if i == '1':
        easy = False
        break
if easy:
    print("EASY")
else:
    print("HARD")
