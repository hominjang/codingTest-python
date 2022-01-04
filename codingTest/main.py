x = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
arr = []
houseCount = []
houseCount2 = []
count = 0

for i in range(x):
    arr.append(list(map(int, input())))


def fun(i, j):
    global count
    arr[i][j] = 2
    count = count + 1
    for k in range(4):
        mx = dx[k] + i
        my = dy[k] + j

        # 범위 밖을 벗어날 때
        if mx < 0 or my < 0 or mx >= x or my >= x:
            continue

        if arr[mx][my] == 0:
            continue

        if arr[mx][my] == 1:
            fun(mx, my)
            houseCount.append(count)
            print(mx, end="")
            print(my)


for i in range(x):
    for j in range(x):
        if arr[i][j] == 1:
            fun(i, j)

arrS = len(houseCount)
houseCount2 = houseCount[:]

for i in range(1, arrS):
    houseCount2[i] = houseCount[i] - houseCount[i - 1]
print(houseCount)
houseCount2.sort()

for i in houseCount2:
    if i != 0:
        print(i)
