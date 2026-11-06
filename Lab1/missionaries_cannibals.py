from collections import deque

def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    rm = 3 - m
    rc = 3 - c
    if rm > 0 and rm < rc:
        return False
    return True

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)
    
    q = deque()
    q.append((start, [start]))
    visited = set()
    visited.add(start)
    
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    
    while q:
        (m, c, boat), path = q.popleft()
        
        if (m, c, boat) == goal:
            return path
        
        for dm, dc in moves:
            if boat == 1:
                new_m = m - dm
                new_c = c - dc
                new_boat = 0
            else:
                new_m = m + dm
                new_c = c + dc
                new_boat = 1
            
            new_state = (new_m, new_c, new_boat)
            
            if valid(new_m, new_c) and new_state not in visited:
                visited.add(new_state)
                q.append((new_state, path + [new_state]))
    
    return None

path = solve()

if path:
    print("Solution found:")
    for i, state in enumerate(path):
        print(i, state)
else:
    print("No solution")
