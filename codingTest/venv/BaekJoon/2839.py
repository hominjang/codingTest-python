a = int(input())
count = 0

while a < 10:
    a = a - 5
    count = count + 1

if a % 3:
    count = count + a / 3
elif a == 5 and a == 8:
    count = count + 1
else:
    count = -1
print(count)
