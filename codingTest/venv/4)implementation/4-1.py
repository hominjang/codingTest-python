num = input()
num = int(num)
ctrl = list(map(str, input().split(" ")))

x = 1
y = 1

for a in range(0, num+1):
    if ctrl[a] == "R" and y < 6:
        y = y + 1

    elif ctrl[a] == "D" and x < 6:
        x = x + 1

    elif ctrl[a] == "L" and y > 1:
        y = y - 1

    elif ctrl[a] == "U" and x > 1:
        x = x - 1

print(str(x) + " " + str(y))
