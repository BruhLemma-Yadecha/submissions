inputs = int(input())
soldiers = input().split()
tallest = 0
tallest_index = -1
shortest = 101
shortest_index = -1
for i, soldier in enumerate(soldiers):
    if int(soldier) > tallest:
        tallest = int(soldier)
        tallest_index = i
for i in range(inputs - 1, -1, -1):
    if int(soldiers[i]) < shortest:
        shortest = int(soldiers[i])
        shortest_index = i
print(f"{shortest_index}, {tallest_index}")
print(tallest_index + (inputs - shortest_index - 1))