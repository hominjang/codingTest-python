x = int(input())
arr = []
left = 0
right = 0
open_close = 0
for i in range(x):
    arr.append(list(map(str, input())))

for i in arr:
    for j in i:
        if j == "(":
            left = left + 1
            open_close = open_close + 1

        if j == ")":
            right = right + 1
            open_close = open_close - 1

        if open_close < 0:
            right = 99999
            break

    if right == left:
        print("YES")
    else:
        print("NO")
    right = 0
    left = 0
    open_close = 0
