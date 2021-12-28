x, y = map(int, input().split(" "))
arr = []

for i in range(x):
    sl = list(map(int, input()))
    arr.append(sl)


def iceCream(currentX, currentY):
    if currentX < 0 or currentX >= x or currentY < 0 or currentY >= y:
        return False

    if arr[currentX][currentY] == 0:
        arr[currentX][currentY] = 1

        iceCream(currentX, currentY - 1)
        iceCream(currentX, currentY + 1)
        iceCream(currentX - 1, currentY)
        iceCream(currentX + 1, currentY)
        return True

    return False


count = 0
for i in range(x):
    for j in range(y):
        if iceCream(i, j) is True:
            count = count + 1
print(count)
