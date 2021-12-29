s = int(input())
list1 = list(map(int, input().split(" ")))

list1.sort()
count = 0
count2 = 0

for i in list1:
    count = count + i
    count2 = count + count2

print (count2)