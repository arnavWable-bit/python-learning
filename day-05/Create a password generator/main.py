import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters=int(input("How many leters would you like in you password? \n"))
nr_symbols=int(input("How many symbols would you like?\n"))
nr_numbers=int(input("How many numbers would you like?\n"))

#EASY

# password=""

# for i in range(1,nr_letters+1) :
#     password += random.choice(letters)
    # random_letter = random.choice(letters)
    # password += random_letter
#    print(random.choice(letters),end="")

# for j in range(1,nr_symbols+1) :
#     password += random.choice(symbols)
    # random_symbol = random.choice(symbols)
    # password += random_symbol
#    print(random.choice(symbols),end="")

# for k in range(1,nr_numbers+1) :
#     password += random.choice(numbers)
    # random_number = random.choice(numbers)
    # password += random_number
#    print(random.choice(numbers),end="")

#print(password)


#HARD

password_list = []
for i in range(1,nr_letters+1) :
    password_list += random.choice(letters)

for j in range(1,nr_symbols+1) :
    password_list += random.choice(symbols)

for k in range(1,nr_numbers+1) :
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list :
    password += char

print(f"Your password is: {password}")