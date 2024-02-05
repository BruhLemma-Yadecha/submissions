levels = int(input())
little_x = input().split()
little_y = input().split()
sovlable = []
found = True
for i in range(1, levels + 1):
    if str(i) not in little_x and str(i) not in little_y:
        found = False
        break
if found:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")