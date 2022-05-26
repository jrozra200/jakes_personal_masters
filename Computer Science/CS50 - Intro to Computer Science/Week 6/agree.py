from cs50 import get_string

c = get_string("Do you agree? ").lower()

if c[0] == "y":
    print("Agreed.")
elif c[0] == "n":
    print("Not agreed.")
