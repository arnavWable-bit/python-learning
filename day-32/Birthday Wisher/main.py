##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import smtplib
import random

# 1. Check if today matches a birthday in the birthdays.csv
birthdays = pd.read_csv("day-32/Birthday Wisher/birthdays.csv")
now = dt.datetime.now()
data = birthdays[
        (birthdays['month']== now.month)
        &
        (birthdays['day']== now.day)
    ] 
   
letter_files = [
    "letter_1.txt",
    "letter_2.txt",
    "letter_3.txt"
]

random_letter = random.choice(letter_files)

# from pathlib import Path

# folder = Path("day-32/Birthday Wisher/letter_templates")

# random_letter = random.choice(list(folder.glob("*.txt")))

# with open(random_letter) as file:
#     content = file.read()

my_email = "wablearnav1@gmail.com"
password = 'fkhc vjak ioyt sjvs'

for index,row in data.iterrows():
    name = row.name
    email = row.email
    
# 2. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(f"day-32/Birthday Wisher/letter_templates/{random_letter}") as letters:
        content = letters.read()
        new_letter = content.replace("[NAME]",name)

# 3. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg= f'Subject:Happy Birthday\n\n{new_letter}'
            )
        
        
        
        
        
        


# ANGELA'S SOLUTION

#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


# from datetime import datetime
# import pandas
# import random
# import smtplib

# MY_EMAIL = "YOUR EMAIL"
# MY_PASSWORD = "YOUR PASSWORD"

# today = datetime.now()
# today_tuple = (today.month, today.day)

# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])

#     with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )