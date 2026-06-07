# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.",
#     123 : "A number"
# }

# print(programming_dictionary["Bug"])
# print(programming_dictionary[123])

# programming_dictionary["Loop"] = "The action of doing something over and over again. "
# print(programming_dictionary)

# empty_dictionary = {}

# Wipe an existing dictionary

# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary

# programming_dictionary["Bug"] = "A moth in your computer. " 
# print(programming_dictionary)


# Loop through a dictionary

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])



capitals = {
    "France" : "Paris" ,
    "Germany" : "Berlin"
}

# Nested list in Dictionary

# travel_log = {
#     "France" : ["Paris", "Lille", "Dijon"],
#     "Germany" : ["Stuttgart", "Berlin"]
# }

# Print Lille
# print(travel_log["France"][1])


# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])


# Nesting a dictionary inside a dictionary

travel_log = {
    "France" : {
        "num_times_visited" : 8,
        "cities_visited" : ["Paris", "Lille", "Dijon"]
    },
    "Germany" : {
        "num_times_visited" : 5,
        "cities_visited" : ["Stuttgart", "Berlin","Hamburg"]
    }
}

print(travel_log["Germany"]["cities_visited"][2])