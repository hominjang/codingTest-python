x = int(input())
arr = []
left = 0
right = 0

for i in range(x):
    arr.append(list(map(str, input())))

for i in arr:
    for j in i:
        if j is "(":
            left = left + 1
        if j is ")":
            right = right + 1

    if right == left:
        print("YES")
    else:
        print("NO")
