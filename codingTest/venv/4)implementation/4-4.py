x, y = map(int, input().split(" "))
locX, locY, locF = map(int, input().split(" "))
listMap = []
stepCheck = [0, 0, 0, 0]
count = 0
step = [(0, -1), (1, 0), (0, 1), (-1, 0)]

for i in range(y):
    listA = list(map(int, input().split(" ")))
    listMap.append(listA)

# 지금 보는 방향에 길을 갈 수 있는지 판단하는 함수 / 갈 수 있다면 전진
while True:

    if locF == 0:
        if listMap[locX][locY - 1] == 1 or listMap[locX][locY - 1] == 2:
            stepCheck[0] = 1
            locF = 3
        else:
            listMap[locX][locY - 1] = 2
            locY = locY - 1
            count = count + 1
            stepCheck = [0, 0, 0, 0]
            continue

    if locF == 1:
        if listMap[locX + 1][locY] == 1 or listMap[locX + 1][locY] == 2:
            stepCheck[1] = 1
            locF = 0
        else:
            listMap[locX + 1][locY] = 2
            locX = locX + 1
            count = count + 1
            stepCheck = [0, 0, 0, 0]
            continue

    if locF == 2:
        if listMap[locX][locY + 1] == 1 or listMap[locX][locY + 1] == 2:
            stepCheck[2] = 1
            locF = 1
        else:
            listMap[locX][locY + 1] = 2
            locY = locY + 1
            count = count + 1
            stepCheck = [0, 0, 0, 0]
            continue

    if locF == 3:
        if listMap[locX - 1][locY] == 1 or listMap[locX - 1][locY] == 2:
            stepCheck[3] = 1
            locF = 2
        else:
            listMap[locX - 1][locY] = 2
            locX = locX - 1
            count = count + 1
            stepCheck = [0, 0, 0, 0]
            continue

    # 현재위치 에서 90도로 도는 함수 / 근처에 길이 없다면 바라보는 방향을 유지한채 뒤로 한칸
    if stepCheck.count(1) == 4:  # 뒤로 미루기
        if locF == 0:
            if listMap[locX][locY + 1] == 1:
                break
            else:
                locY = locY + 1
                stepCheck = [0, 0, 0, 0]
                continue

        if locF == 1:
            if listMap[locX-1][locY] == 1:
                break
            else:
                locX = locX - 1
                stepCheck = [0, 0, 0, 0]
                continue

        if locF == 2:
            if listMap[locX][locY - 1] == 1:
                break
            else:
                locY = locY - 1
                stepCheck = [0, 0, 0, 0]
                continue

        if locF == 3:
            if listMap[locX+1][locY] == 1:
                break
            else:
                locX = locX + 1
                stepCheck = [0, 0, 0, 0]
                continue

print(count)
