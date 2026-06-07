import random
word_list = ["baboon", "camel", "aardvark"]

chosen_word = random.choice(word_list)
print(chosen_word)

# placeholder_list = []
# for blanks in chosen_word :
#     placeholder_list.append("_")

placeholder = ""

for blank in chosen_word :
    placeholder += "_"

print(placeholder)

# TODO-1 - Use a while loop to let user guess again

game_over = False
display = placeholder
#correct_letters = []

while not game_over:

    old_display= display  
    display = ""

    guess = input("Guess a letter: ").lower()

    # TODO-2 - Change the for loop so that you keep the previous corrected letters in display.
    position = 0

    for letter in chosen_word :
        if letter == guess :
            display += letter
            # correct_letters.append(guess)
        elif old_display[position] != "_" :                    #elif letter in correct_letters:
            display += old_display[position]                        #display += letter
        else :
            display += "_"

        position += 1

    print(display)

    if "_" not in display :
        game_over = True
        print("You win!")