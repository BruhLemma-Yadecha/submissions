time = input().split(" ")[1]
queue_in = input()
queue = []
for c in queue_in:
    queue.append(c)

for i in range(0, int(time), 2):
    for j in range(0, len(queue) - 1):
        if queue[j] == 'B' and queue[j + 1] == 'G':
            queue[j] = 'G'
            queue[j + 1] = 'B'
print("".join(queue))
