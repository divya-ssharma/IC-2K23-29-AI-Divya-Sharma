import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {'F': 1},
    'E': {'F': 2},
    'F': {}
}

h = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 1,
    'E': 2,
    'F': 0
}

def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + h[start], 0, start, [start]))
    visited = set()
    
    while open_list:
        f, g, node, path = heapq.heappop(open_list)
        if node in visited:
            continue
        visited.add(node)
        
        if node == goal:
            return path
        
        for nei, cost in graph[node].items():
            if nei not in visited:
                new_g = g + cost
                new_f = new_g + h[nei]
                heapq.heappush(open_list, (new_f, new_g, nei, path + [nei]))
    
    return None

print(astar('A', 'F'))
