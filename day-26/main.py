# List comprehension

numbers = [1,2,3]

# new_list = [new_item for item in list]
# Create a new list from numbers ,where you added 1 to each value
# new_list = [n+1 for n in numbers]
# print(new_list)

# name = 'Angela'
# new_list = [letter for letter in name]
# print(new_list)


# new_list = [i*2 for i in range(1,5)]
# print(new_list)


# Conditional List Comprehension
# new_list = [new_item for item in list if test]

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [name for name in names if len(name) < 5]
# print(short_names)

# create a list that contains the names longer than 5 characters in ALL CAPS
# all_caps = [name.upper() for name in names if len(name) > 5]
# print(all_caps)





# Dictionary Comprehension
# new_dict = {new_key : new_value for item in list}
# new_dict = {new_key : new_value for (key,value) in dict.items() if test}

# import random

# students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)

# passed_students = {student:score for (student,score) in students_scores.items() if score >= 60}
# print(passed_students)




# How to iterate over a Pandas DataFrame

student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56,76,98]
}

# Looping through dictionaries

# for (key,value) in student_dict.items():
#     print(value)
#     print(key)

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)

# Loop through a data frame

# for (key,value) in student_data_frame.items():
#     print(value)
#     print(key)

# Loop through rows of a dataframe
# for(index,row) in student_data_frame.iterrows():
#     print(row)
#     print(row.student)
#     print(row.score)
#     if row.student == "Angela":
#        print(row.score)

