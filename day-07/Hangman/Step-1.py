import random
word_list = ["baboon", "camel", "aardvark"]

# TODO-1 -Randomly choose a word from the word_list and assign it to a variable called chosen_word . Then print it.

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()

# TODO-3 - Check if the letter user guessed (guess) is one of the letters in chosen_word. Print "Right" if it is and "Wrong" if it is not.

for letter in chosen_word:
    if letter == guess :
        print("Right")
    else :
        print("Wrong")