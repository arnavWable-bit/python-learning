import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images=[rock,paper,scissors]

my_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scisssors\n"))

if my_choice >=0 and my_choice <=2 :
    print(game_images[my_choice])

comp_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[comp_choice])

if my_choice >=3 or my_choice < 0:
    print("You typed an invalid number. You lose!")
elif my_choice==comp_choice :
    print("Draw")
elif my_choice == 0 and comp_choice == 2 :
    print("You win!")
elif my_choice == 1 and comp_choice == 0 :
    print("You win!")
elif my_choice == 2 and comp_choice == 1 :
    print("You win!")
else :
    print("You lose!")