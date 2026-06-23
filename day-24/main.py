# file = open("day-24/my_file.txt")
# with open("day-24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# with open("day-24/my_file.txt", mode='a') as file:    # mode = w if you want to delete the previous texts and add the new one.
#     file.write("\nNew text.")


# when you are using w for a file that doesnt exist , it will create a new file from scratch
with open("day-24/new_file.txt", mode='w') as file:
    file.write("New text.")