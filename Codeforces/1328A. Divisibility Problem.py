number_of_lines = int(input())
lines = []
for i in range(number_of_lines):
    lines.append(input().split())
for line in lines:
    moves = 0
    a = int(line[0])
    b = int(line[1])
    if a % b == 0:
        print(0)
    else:
        print(b - a % b)