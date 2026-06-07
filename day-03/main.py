#CHECK ODD EVEN

# num=int(input("type a number to check: "))
# if(num % 2 == 0) :
#     print("num is even")
# else :
#     print("num is odd")



# IF-ELSE

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill=0

# if height >= 120 :
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 12 :
#         bill=5
#         print("child tickets are $5.")
#     elif age <= 18 :
#         bill=7
#         print("Youth tickets are $7.")
#     else:
#         bill=12
#         print("Adult tickets are $12.")

#     wants_photo=input("Do you want to have a photo take? Type y for Yes and n for No ")

#     if wants_photo == "y":
#         #Add $3 to bill
#         bill+=3

#     print(f"Total bill is: ${bill}")
# else :
#     print("Sorry you have to grow taller before tou ride")




# PIZZA DELIVERY PROGRAM

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want ? S, M or L: ")
# pepperoni = input("Do you want pepperono on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# bill=0

# if size == "S":
#     bill = 15
#     #print("Small size pizzas are for $15.")
    
#     if pepperoni == "Y":
#         bill += 2

# elif size == "M":
#     bill = 20
#     #print("Medium size pizzas are for $20.")
# elif  size == "L" :
#     bill = 25
#     #print("Large size pizzas are for $25.")
# else:
#     print("You typed the wrong inputs. ")

# if pepperoni == "Y":
#     bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your total bill is: ${bill}")



# MODIFYING ROLLER COASTER USING LOGICAL OPERATORS

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0

if height >= 120 :
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12 :
        bill=5
        print("child tickets are $5.")
    elif age <= 18 :
        bill=7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:                                           # 45 <= age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill=12
        print("Adult tickets are $12.")

    wants_photo=input("Do you want to have a photo take? Type y for Yes and n for No ")

    if wants_photo == "y":
        #Add $3 to bill
        bill+=3

    print(f"Total bill is: ${bill}")
else :
    print("Sorry you have to grow taller before tou ride")

