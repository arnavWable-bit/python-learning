import smtplib
import random

# my_email = "wablearnav1@gmail.com"
# password = 'fkhc vjak ioyt sjvs'
# # fkhc vjak ioyt sjvs

# #connection = smtplib.SMTP("smtp.gmail.com")
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="appbrewerytesting@yahoo.com",
#         msg='Subject:Hello\n\nThis is the body of my email.')

#connection.close()



import datetime as dt

# now = dt.datetime.now()
# year = now.year
# # print(now)
# # print(year)
# # print(type(now))
# # print(type(year))
# if year == 2026:
#     print("Hi there")

# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=2006, month=5, day=8)
# print(date_of_birth)


# SEND MOTIVATIONAL QUOTE AUTOMATICALLY
now = dt.datetime.now()
weekday = now.weekday()
my_email = "wablearnav1@gmail.com"
password = 'fkhc vjak ioyt sjvs'


if weekday == 7:
    with open("day-32/Sending mail/quotes.txt") as file:
        all_quotes = file.readlines()  
        quote = random.choice(all_quotes)


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="arnavwable9@gmail.com",
            msg= f'Subject:Motivatinal Quote\n\n{quote}'
            )



