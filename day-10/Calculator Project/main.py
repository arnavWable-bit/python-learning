from art import logo
print(logo)


# 1st METHOD

# restart_program = True
# while restart_program :

#     first_number = float(input("What's the first number?: "))

#     def calculate(first_number, next_number,operation) :
#         if operation == '+':
#             return first_number + next_number
#         elif operation == '-':
#             return first_number - next_number
#         elif operation == '*':
#             return first_number * next_number
#         else :
#             return first_number / next_number



#     should_continue = True
#     while should_continue:
#         print("+")
#         print("_")
#         print("*")
#         print("/")

#         operation = input("Pick an operation:  ")

#         next_number = float(input("What's the next number?: "))

#         result = calculate(first_number, next_number, operation)

#         print(f"{first_number} {operation} {next_number} = {result}")

#         what_to_do = input(f"Type 'y' to continue calculating with {result} , or type 'n' to start a new calculation: ")
        
#         if what_to_do == 'y':
#             first_number = result
#         else:
#             should_continue = False
#             print("\n" *50)
            

            





# 2nd METHOD



def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

# print(operations["*"](4,3))

def calculator():
    first_number = float(input("What's the first number?: "))

    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)

        operation = input("Pick an operation:  ")

        next_number = float(input("What's the next number?: "))

        operation_function = operations[operation]
        result = operation_function(first_number, next_number)

        print(f"{first_number} {operation} {next_number} = {result}")
        
        what_to_do = input(f"Type 'y' to continue calculating with {result} , or type 'n' to start a new calculation: ")
        if what_to_do == 'y':
            first_number = result
        else:
            print("\n" * 50)
            calculator()

calculator()