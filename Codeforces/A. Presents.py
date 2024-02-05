people = int(input())
gifts = input().split(" ")
result = gifts.copy()
current_giver = 1
for recipient in gifts:
    result[int(recipient) - 1] = str(current_giver)
    current_giver += 1

print(f'{" ".join(result)}')
