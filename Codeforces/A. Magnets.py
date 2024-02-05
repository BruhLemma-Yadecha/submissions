magnet_count = int(input())
last_magnet = input()
groups = 0
for i in range(magnet_count - 1):
    magnet = input()
    if magnet != last_magnet:
        groups += 1
        last_magnet = magnet
if groups == 0:
    print(1)
else:
    print(groups + 1)