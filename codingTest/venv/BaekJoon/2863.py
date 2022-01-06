arr = []

max = 0
maxIndex = 0

a, b = map(int, input().split())
c, d = map(int, input().split())

queue = [a, b, c, d]
changeQ = []

for _ in range(4):
    sum1 = (queue[0] / queue[2]) + (queue[1] / queue[3])
    arr.append(sum1)
    changeQ = [queue[2], queue[0], queue[3], queue[1]]
    queue = changeQ[:]

for index, value in enumerate(arr):
    if (max < value):
        max = value
        maxIndex = index

print(maxIndex)
