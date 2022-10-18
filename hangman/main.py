import re


# get the answer
answer = "What's up, Doc?"

answer = answer.upper()

# pre game setup
answer_guessed = []

# this loop is to show the special charactaers (not A-Z letters) to the user
for current_answer_character in answer:
    if re.search("^[A-Z]$", current_answer_character):
        answer_guessed.append(False)
    else:
        answer_guessed.append(True)

# game logic
num_of_incorrect_guesses = 5

current_incorrect_guesses = 0

letters_guessed = []

# user gameplay logic
while current_incorrect_guesses < num_of_incorrect_guesses and False in answer_guessed:
    # display game summary
    print(f"Number of incorrect guesses remaining: {num_of_incorrect_guesses - current_incorrect_guesses}")