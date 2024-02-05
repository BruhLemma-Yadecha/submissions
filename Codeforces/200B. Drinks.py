number_of_drinks = int(input())
drinks = input().split()
juice = 0
for drink in drinks:
    juice += int(drink)
result = juice / (int(number_of_drinks))
print(result)