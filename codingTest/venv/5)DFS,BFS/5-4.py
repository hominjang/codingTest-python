# DFS
def dfs(a, b, c):
    visited[c] = True
    print(c)

    # 인접노드를 찾는 반복문
    for i in graph[c]:
        # 방문하지 않은 노드를 찾는 조건문
        if not visited[i]:
            dfs(a, b, i)


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
dfs(graph, visited, 1)