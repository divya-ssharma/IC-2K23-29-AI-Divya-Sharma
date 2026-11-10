facts = set()

rules = [
    (['fever', 'cough'], 'flu'),
    (['fever', 'rash'], 'measles'),
    (['sore_throat', 'fever'], 'strep'),
    (['flu'], 'rest'),
    (['measles'], 'isolation')
]

print("symptoms (done to stop)")
while True:
    s = input().strip().lower()
    if s == 'done':
        break
    facts.add(s)

changed = True
while changed:
    changed = False
    for condition, result in rules:
        if all(c in facts for c in condition) and result not in facts:
            facts.add(result)
            print("->", result)
            changed = True

print(facts)
