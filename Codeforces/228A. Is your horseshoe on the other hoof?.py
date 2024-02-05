shoes = input().split()
shoes_explored = []
for shoe in shoes:
    if shoe not in shoes_explored:
        shoes_explored.append(shoe)
print(4 - len(shoes_explored))