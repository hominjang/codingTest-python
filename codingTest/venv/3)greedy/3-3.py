n, m = map(int, input().split())
sumA = 0
Max = 0

for i in range(1, n + 1):
    listA = list(map(int, input().split()))
    listA.sort()
    if listA[0] > Max:
        Max = listA[0]

print(Max)
