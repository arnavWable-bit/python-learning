# def greet() :
#     print("Hello")
#     print("What's up?")
#     print("How do you do?")

# greet()

 # Function that allows input

# def greet_with_name(name) :
#     print(f"Hello {name}")
#     print(f"What's up {name} ?")
#     print(f"How do you do {name} ?")

# greet_with_name("Arnav")


# Function that allows more than 1 input

# def greet(name, location) :
#     print(f"Hello {name}!")
#     print(f"What is it like in {location}?")

# greet("Arnav", "France")

#Positional argument
# greet("France" ,"Arnav")            # That doesn't make sense

#Keyword Arguments
# greet(location="France", name="Arnav")


def calculate_love_score(name1,name2) :
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")

    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)

calculate_love_score("Kanye West", "Kim Kardashian")