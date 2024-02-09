first_line = input().split()
n = int(first_line[0])
t = int(first_line[1])
arrangement = input()
arrangement = list(arrangement)
while t > 0:
    new_arrangement = []
    i = 0
    while i < n - 1:
        if arrangement[i] == 'B' and arrangement[i + 1] == 'G':
            new_arrangement.append('G')
            new_arrangement.append('B')
            i += 2
        else:
            new_arrangement.append(arrangement[i])
            i += 1
    if len(new_arrangement) != len(arrangement):
        new_arrangement.append(arrangement[n - 1])
    arrangement = new_arrangement
    t -= 1
print("".join(arrangement))
