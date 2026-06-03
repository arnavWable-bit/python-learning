print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")

direction=input("You're at cross road.Where do you want to go?\n     Type'left' or'right' \n").lower()

if direction == "left":
    what_to_do=input("You've come to a lake. There is an island in the middle of the lake.\n" \
    "  Type 'wait' to wait for a boat. Type 'swim' to swim across \n").lower()

    if what_to_do == "wait" :
        choose = input("You arrive at the island unharmed. There is a house with 3 doors.\n " \
        " One red, one yellow and one blue. Which color do you choose? \n").lower()

        if choose == "red":
            print("It's a room full of fire. Game Over!")
        elif choose == "yellow":
            print("You Win!")
        elif choose == "blue":
            print("You entered a room full of beasts. Game Over!")
        else:
            print("You choose a door that doesn't exist. Game Over!")

    else:
        print("Game Over.")

else:
    print("Game Over.")