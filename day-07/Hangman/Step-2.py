import random
word_list = ["baboon", "camel", "aardvark"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1 - Create a "placeholder" with the same number of blanks as the number of letters in chosen_word

# placeholder_list = []
# for blanks in chosen_word :
#     placeholder_list.append("_")

placeholder = ""

for blank in chosen_word :
    placeholder += "_"

print(placeholder)

guess = input("Guess a letter: ").lower()

# TODO-2 - Create a "display" that puts the guess letter in the right block and _ in rest .

display = ""

for letter in chosen_word :
    if letter == guess :
        display += letter
    else :
        display += "_"

print(display)