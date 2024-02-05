def beautiful(n):
    digits = []
    while n != 0:
        digit = n % 10
        if digit in digits:
            return False
        else:
            digits.append(digit)
        n //= 10
    return True

year = int(input()) + 1
while not beautiful(year):
      year += 1
print(year)

