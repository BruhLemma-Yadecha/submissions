cases = int(input())
for i in range(cases):
    length = int(input())
    numbers = input().split()
    # greed
    i = 0
    result = []
    while i < len(numbers):
        new_list = []
        local_sum = 0
        while i < len(numbers) and local_sum != 0:
            value = 1
            if numbers[i] == '-':
                value = -1
            new_list.append(value)
            local_sum += value
            i += 1
        result.append(new_list)
        i += 1
    print(len(result))
        
        
