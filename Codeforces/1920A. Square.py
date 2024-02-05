number_of_squares = int(input())
squares = []
for i in range(number_of_squares):
    vertices = []
    for j in range(0, 4):
        vertices.append(input().split())
    squares.append(vertices)
for square in squares:
    x_max = int(square[0][0])
    x_min = x_max
    for vertex in square:
        x_max = max(int(vertex[0]), x_max)
        x_min = min(int(vertex[0]), x_min)
    print((x_max - x_min) ** 2)
    