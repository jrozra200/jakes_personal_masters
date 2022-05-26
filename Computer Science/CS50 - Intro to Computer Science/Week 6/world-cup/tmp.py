import csv
import sys

teams = []
# Read teams into memory from file
with open(filename, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        team = row["team"]
        rating = int(row["rating"])
        teams.append({"team":team, "rating":rating})

print(teams)
