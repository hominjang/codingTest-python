a = int(input())
b = int(input())
list1 = [[] for _ in range(a+1)]
visited = [False] * (a + 1)
count = 0

for i in range(b):
    x, y = (map(int, input().split(" ")))
    list1[x].append(y)
    list1[y].append(x)

print (list1)

def bfs(node):
    global count
    visited[node] = True
    for i in list1[node]:
        if not visited[i]:
            count = count + 1
            bfs(i)


bfs(1)
print(count)

# 1인거를 찾자
# 연계되는 거를 찾고
