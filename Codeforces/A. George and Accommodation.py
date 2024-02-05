number_of_arguments = int(input())
rooms = []
for i in range(number_of_arguments):
    rooms.append(input())
result = 0;
for r in rooms:
    room = r.split(' ')
    occupants = int(room[0])
    capacity = int(room[1])
    if occupants + 2 <= capacity:
        result += 1
print(result)