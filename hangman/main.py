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

    print ("Guessed letters: ", end="") # end by default is new line, here dont endl, don't do anything

    for current_letter_guessed in letters_guessed:
        print(current_letter_guessed, end=" ")
    
    print()

    # display puzzle board
    for current_answer_index in range(len(answer)):
        if answer_guessed[current_answer_index]:
            print(answer[current_answer_index], end="")
        else:
            print("_", end="")

    print()

    # let user guess a letter
    letter = input("enter a letter")

    letter = letter.upper()

    # check if user entered a valid letter
    if re.search("^[A-Z]$", letter) and len(letter) == 1 and letter not in letters_guessed:
        # insert the letter guessed by the user (insertion sort)
        current_letter_index = 0
        for current_letter_guessed in letters_guessed:
            if letter < current_letter_guessed:
                break
            current_letter_index += 1

        letters_guessed.insert(current_letter_index, letter)

        # check if letter is in the puzzle
        if letter in answer:
            for current_answer_index in range(len(answer)):
                if letter == answer[current_answer_index]:
                    answer_guessed[current_answer_index] = True
        else:
            current_incorrect_guesses += 1

# post-game summary
if current_incorrect_guesses < num_of_incorrect_guesses:
    print("you won")
else:
    print(f"you lost, the answer was {answer}")

