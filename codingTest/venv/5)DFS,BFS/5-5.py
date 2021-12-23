# BFS
from collections import deque


def bfs(a, b, c):
    queue = deque([c])
    visited[c] = True

    while queue:  # 큐가 돌때까지

        # 큐에서 숫자 꺼내서 확인
        v = queue.popleft()
        print(v)

        # 인접노드를 찾는 반복문
        for i in graph[v]:
            # 방문하지 않은 노드를 찾는 조건문
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9
bfs(graph, visited, 1)