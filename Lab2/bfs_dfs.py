from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(start, goal):
    q = deque([[start]])
    visited = set([start])
    while q:
        path = q.popleft()
        node = path[-1]
        if node == goal:
            return path
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                new_path = list(path)
                new_path.append(nei)
                q.append(new_path)
    return None

def dfs(start, goal):
    stack = [[start]]
    visited = set()
    while stack:
        path = stack.pop()
        node = path[-1]
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path
        for nei in reversed(graph[node]):
            new_path = list(path)
            new_path.append(nei)
            stack.append(new_path)
    return None

print("BFS:", bfs('A', 'F'))
print("DFS:", dfs('A', 'F'))
