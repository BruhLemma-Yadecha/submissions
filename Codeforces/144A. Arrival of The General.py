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
for i, soldier in reversed(list(enumerate(soldiers))):
    if int(soldier) < shortest:
        shortest = int(soldier)
        shortest_index = i

# check if the shortest is actually to the right of the tallest
# if so, they won't get affected by shuffling the tallest one up
tallest_distance = tallest_index
shortest_distance = len(soldiers) - 1 - shortest_index
if tallest_index < shortest_index:
    # business as usual, print out
    print(tallest_distance + shortest_distance)
else:
    # they'll affect eachother
    # the shortest will push the tallest one step as he passes
    # so account for this by adding a -1
    print(tallest_distance + shortest_distance - 1)
