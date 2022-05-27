# Libraries
from cs50 import get_string

# Get text from user
text = get_string("Text: ")

# Set counters equal to 0 (or false)
letters = 0
words = 0
sentences = 0
last_letter_is_break = False

# Count the letters, words, and sentences
for c in range(len(text)):
    if (text[c] == " " or text[c] in [".", "!", ",", ";", ":", "?"]) and last_letter_is_break != True:
        words += 1
        last_letter_is_break = True
    if text[c].lower() >= 'a' and text[c].lower() <= 'z':
        letters += 1
        last_letter_is_break = False
    if text[c] == text[c] in [".", "!", "?"]:
        sentences += 1
        last_letter_is_break = True
        
# Calculate the L, S, and index
L = (letters / words) * 100
S = (sentences / words) * 100
index = 0.0588 * L - 0.296 * S - 15.8

# Convert into a "Grade"
if index > 16.0:
    grade = "Grade 16+"
elif index < 1:
    grade = "Before Grade 1"
else:
    grade = "Grade " + str(int(round(index, 0)))

# Print Grade    
print(grade)
