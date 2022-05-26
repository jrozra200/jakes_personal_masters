from cs50 import get_int

points = get_int("How many points did you lose? ")

if points < 2:
    print("You lost fewer points than me.")
elif points > 2:
    print("You lost more points than me.")
else:
    print("You lost the same points as me.")
