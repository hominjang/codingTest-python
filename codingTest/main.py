n, m = map(int, input().split())  # n은 리스트 크기 , m은 횟수, k는 최소 반복
sumA = 0
Max = 0

for i in range(1, n + 1):
    listA = list(map(int, input().split()))
    listA.sort()
    if listA[0] > Max:
        Max = listA[0]

print(Max)
