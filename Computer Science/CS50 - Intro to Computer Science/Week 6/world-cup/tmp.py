import csv
import sys

filename = "2018m.csv"

teams = []
# Read teams into memory from file
with open(filename, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(len(row))
        team = row["team"]
        rating = int(row["rating"])
        teams.append({"team":team, "rating":rating})

print(teams)
