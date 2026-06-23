#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
        
with open("day-24/Mail Merge Project/Input/Letters/starting_letter.txt") as letter:
    contents = letter.read()
        
with open("day-24/Mail Merge Project/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

    
for name in names:
    name = name.strip()
    new_letter = contents.replace("[name]", name)
    with open(f"day-24/Mail Merge Project/Output/ReadyToSend/letter_for_{name}.txt", mode='w') as letters:  
        letters.write(new_letter)


