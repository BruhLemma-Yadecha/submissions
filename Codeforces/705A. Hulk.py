n = int(input())
hate = True
for i in range(n - 1):
    if hate:
        print("I hate that", end = " ")
        hate = False
    else:
        print("I love that", end = " ")
        hate = True
if hate:
        print("I hate it")
else:
    print("I love it")