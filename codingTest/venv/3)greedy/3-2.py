n, m, k = map(int, input().split()) # n은 리스트 크기 , m은 횟수, k는 최소 반복
sumA = 0
listA = list(map(int, input().split()))

listA.sort()

if listA[n-1] != listA[n-2]:
    for i in range(1,m+1):
        if i % k == 0 :
            sumA = listA[n-2] + sumA
        else :
            sumA = listA[n-1] + sumA
else:
    for i in range(1,m):
            sumA = listA[n-1] + sumA


print(sumA)
