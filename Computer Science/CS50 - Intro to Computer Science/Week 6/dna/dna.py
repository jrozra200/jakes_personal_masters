import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py DATABASE SEQUENCE")
        sys.exit(1)

    # Read database file into a variable
    # Create a list of dicts for the database
    fields = []
    rows = []
    # Open the file and read rows and header
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file, delimiter=",")
        fields = next(reader)
        for row in reader:
            rows.append(row)

    # Combine them into a list of dicts
    db = []
    for row in range(len(rows)):
        tmp = {}
        for field in range(len(fields)):
            if field > 0:
                tmp[fields[field]] = int(rows[row][field])
            else:
                tmp[fields[field]] = rows[row][field]
        db.append(tmp)

    # Read DNA sequence file into a variable sys.argv[2]
    with open(sys.argv[2], "r") as file:
        reader = csv.reader(file, delimiter=",")
        sequence = str(next(reader)[0])

    # Find longest match of each STR in DNA sequence
    strs = list(db[0].keys())
    strs.remove("name")

    match_stats = {}
    for sts in strs:
        match_stats[sts] = longest_match(sequence, sts)

    # Check database for matching profiles
    matches = {}
    for peep in range(len(db)):
        person = db[peep]["name"]
        matches[person] = 0
        for sts in range(len(strs)):
            gataca = strs[sts]
            if db[peep][gataca] == match_stats[gataca]:
                matches[person] += 1

        if matches[person] == len(strs):
            print(person)
            sys.exit(0)

    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
