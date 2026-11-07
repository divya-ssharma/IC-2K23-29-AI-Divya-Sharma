import random

def heuristic(state):
    return abs(state - 10)

def hill_climbing():
    current = random.randint(0, 20)
    print("start:", current)
    
    while True:
        neighbors = [current-1, current+1]
        next_state = current
        best_h = heuristic(current)
        
        for n in neighbors:
            if 0 <= n <= 20:
                h = heuristic(n)
                if h < best_h:
                    best_h = h
                    next_state = n
        
        if next_state == current:
            break
        current = next_state
        print("moved to:", current)
    
    print("final:", current)

hill_climbing()
