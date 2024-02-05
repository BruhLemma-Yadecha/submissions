line0 = input()
line1 = input()

fence_height = line0.split(" ")[1]
person_heights = line1.split(" ")

width = 0
for person_height in person_heights:
    if int(person_height) > int(fence_height):
        width += 2
    else:
        width += 1
print(width)