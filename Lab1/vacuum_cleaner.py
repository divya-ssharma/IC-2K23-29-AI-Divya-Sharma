print("Enter Clean or Dirty")
a = input("Room A status: ").strip().capitalize()
b = input("Room B status: ").strip().capitalize()
loc = input("Vacuum location (A or B): ").strip().upper()

print("\nStarting...")
print("A:", a, " B:", b, " Vacuum at:", loc)

if loc == "A":
    if a == "Dirty":
        print("Sucking dirt in A")
        a = "Clean"
    if b == "Dirty":
        print("Moving to B")
        loc = "B"
        print("Sucking dirt in B")
        b = "Clean"

elif loc == "B":
    if b == "Dirty":
        print("Sucking dirt in B")
        b = "Clean"
    if a == "Dirty":
        print("Moving to A")
        loc = "A"
        print("Sucking dirt in A")
        a = "Clean"
else:
    print("wrong location")

print("\nFinal:")
print("A:", a, " B:", b, " Vacuum at:", loc)

if a == "Clean" and b == "Clean":
    print("Both rooms clean")
