# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()

#     #print(f"{formatted_f_name} {formatted_l_name}")
#     return f"{formatted_f_name} {formatted_l_name}"

# full_name = format_name("aRnAV","WABLE")
# print(full_name)




# def function_1(text):
#     return text + text


# def function_2(text):
#     return text.title()


# output = function_2(function_1("hello"))
# print(output)




# MULTIPLE RETURN 
def format_name(f_name, l_name):
    """Take a first and last name and format it to
    return the title case version of the name. """                                                  # DOC STRING
    
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name?"), input("What is your last name?")))




# LEAP YEAR
# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
