money = input()
money = int(money)

coin = [500, 100, 50, 10]
count = 0
for coin1 in coin:
    count = money // coin1 + count
    money = money % coin1

print(count)
