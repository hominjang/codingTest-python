num = input()

x = int(num[1])
y = int(ord(num[0])) - 96

count = 0

if 2 < x < 6:  # 3,4,5,6
    if y == 1 or y == 8:
        count = 8
    elif y == 2 or y == 7:
        count = 12
    else:
        count = 16

else:  # 1,2 / 7,8
    if y == 1 or y == 8:
        count = 4
    elif y == 2 or y == 7:
        count = 6
    else:
        count = 12

print(count)
