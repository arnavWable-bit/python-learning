from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]


    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    Mail = mail_entry.get()
    Pass = password_entry.get()
    
    if len(web)==0 or len(Pass) == 0:
        messagebox.showinfo(title="Oops", message="Please don’t leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title= web, message= f"These are the details entered: \nEmail: {Mail}"
                                    f"\nPassword: {Pass}\n Is it ok to save?")
        
        if is_ok:
            with open("day-29/data.txt", mode='a') as file:
                file.write(f"{web} | {Mail} | {Pass} \n")
                website_entry.delete(0, END) 
                password_entry.delete(0, END)
            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="day-29/Password Manager Project/logo.png")
canvas.create_image(100,100, image= lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:",font=("Arial", 18))
website_label.grid(column=0, row=1)

mail_label = Label(text="Email/Username:",font=("Arial", 18))
mail_label.grid(column=0, row=2)

password_label = Label(text="Password:",font=("Arial", 18))
password_label.grid(column=0, row=3)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(column=2, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

mail_entry = Entry(width=35)
mail_entry.grid(column=1, row=2, columnspan=2)
mail_entry.insert(0, "arnav@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)



window.mainloop()