k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input()) + 1
dragons = [x for x in range(1, d) if x % k != 0 and x % l != 0 and x % m != 0 and x % n != 0]
damaged = len(range(1, d)) - len(dragons)
print(damaged)
