case_count = int(input())
cases = []
for i in range(case_count):
    length = input()
    s = input().lstrip('W').rstrip('W')
    cases.append(s)

for case in cases:
    print(len(case))
