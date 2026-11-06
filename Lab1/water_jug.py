jug1 = 4
jug2 = 3

a = 0
b = 0

print("start:", a, b)

while True:
    if a == 2 or b == 2:
        print("got the target")
        break

    if a == 0:
        a = jug1
        print("filled jug1 ->", a, b)
    
    elif b == jug2:
        b = 0
        print("emptied jug2 ->", a, b)
    
    else:
        space = jug2 - b
        if a <= space:
            b = b + a
            a = 0
        else:
            a = a - space
            b = jug2
        print("poured ->", a, b)

print("final:", a, b)
