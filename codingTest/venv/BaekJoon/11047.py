x, y = map(int, input().split())
count = 0
arr = []
for _ in range(x):
    arr.append(int(input()))

arr.reverse()

for i in arr:
    if (y < i):
        continue

    while (y >= i):
        y = y - i
        count = count + 1

    if i == 0:
        break

print(count)
