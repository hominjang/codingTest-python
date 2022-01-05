x = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
arr = []
houseCount = []

count = 0

for i in range(x):
    arr.append(list(map(int, input())))


def fun(i, j):
    global count
    # 범위 밖을 벗어날 때
    if i < 0 or j < 0 or i >= x or j >= x:
        return False

    if arr[i][j] == 0:
        return False

    if arr[i][j] == 1:
        arr[i][j] = 0
        count = count + 1
        for k in range(4):
            mx = dx[k] + i
            my = dy[k] + j
            fun(mx, my)
        return True
    return False


for i in range(x):
    for j in range(x):
        if fun(i, j):
            houseCount.append(count)
            count = 0

print(len(houseCount))
for i in houseCount:
    print(i)
