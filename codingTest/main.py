from collections import deque

x, y = map(int, input().split(" "))
arr = []

for i in range(x):
    sl = list(map(int, input()))
    arr.append(sl)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bps():
    queue = deque()
    queue.append((0, 0))
    arr[0][0] = 0
    while queue:
        dequeX = queue.popleft()
        print(dequeX, end=" ")
        dequeY = queue.popleft()
        print(dequeY)

        for I in range(4):
            X = dequeX + dx[I]
            Y = dequeY + dy[I]

            if X < 0 or Y < 0 or Y > y - 1 or X > x - 1:
                continue

            if arr[X][Y] == 0:
                continue

            if arr[X][Y] == 1:
                arr[X][Y] = arr[dequeX][dequeY] + 1
                queue.append(x)
                queue.append(y)

        # 방문큐의 주위 탐색
        # if arr[dequeX + 1][dequeY] == 1:
        #     arr[dequeX + 1][dequeY] = 0
        #     queue.append([dequeX + 1, dequeY])
        #     count1 = count1 + 1
        #
        # if arr[dequeX - 1][dequeY] == 1:
        #     arr[dequeX - 1][dequeY] = 0
        #     queue.append([dequeX - 1, dequeY])
        #     count1 = count1 + 1
        #
        # if arr[dequeX][dequeY + 1] == 1:
        #     arr[dequeX][dequeY + 1] = 0
        #     queue.append([dequeX, dequeY + 1])
        #     count1 = count1 + 1
        #
        # if arr[dequeX][dequeY - 1] == 1:
        #     arr[dequeX][dequeY - 1] = 0
        #     queue.append([dequeX, dequeY - 1])
        #     count1 = count1 + 1

        # 만약 디큐 값이 x,y 였을 때
    return arr[x - 1][y - 1]


print(bps())
