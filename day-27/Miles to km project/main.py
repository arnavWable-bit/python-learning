from tkinter import *

def button_clicked():
    miles = float(input.get())
    km = round(miles * 1.609)
    label4.config(text= f'{km}')

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

label1 = Label(text="Miles",font=("Arial", 24, "bold"))  
label1.grid(column=2, row=0)

label2 = Label(text="km",font=("Arial", 24, "bold"))  
label2.grid(column=2, row=1)

label3 = Label(text="is equal to",font=("Arial", 24, "bold"))  
label3.grid(column=0, row=1)

label4 = Label(text= 0,font=("Arial", 24, "bold"))  
label4.grid(column=1, row=1)

button = Button(text='Calculate', command= button_clicked)
button.grid(column=1, row=2)

input = Entry(width=10)
input.grid(column=1, row=0)






window.mainloop()