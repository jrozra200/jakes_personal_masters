import csv
from cs50 import get_string

name = get_string("Name: ")
number = get_string("Number: ")

with open("phonebook.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, number])
    
## For the hogwarts example
with open("hogwarts.csv", "r") as file:
    reader = csv.DictReader(file)
    next(reader)
    for row in reader:
        house = row["House"]
        houses[house] += 1

# from cs50 import get_string
# 
# people = {
#     "Carter": "+1-617-495-1000",
#     "David": "+1-949-468-2750"
# }
# 
# name = get_string("Name: ")
# if name in people:
#     print(f"Number: {people[name]}")
#     
