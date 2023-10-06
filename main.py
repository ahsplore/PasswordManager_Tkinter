from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Verdana"
WHITE = "#fff"


# PASSWORD GENERATOR --->

def generate_password():
    letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i',
               'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r',
               'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
    symbols = ['!', '@', '$', '%', '^', '&', '*', '(', ')', '{', '[', '|', '\\', ', ', '?', '/', '_',
               '-', '~', '`', '>', ',', '<', '.', '+', ';', '=', ']', '}']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    print("Welcome to password generator")
    Letter_ = random.randint(8, 10)
    Symbol_ = random.randint(2, 4)
    Number_ = random.randint(2, 4)

    password_list = []
    pass1 = [random.choice(letters) for _ in range(0, Letter_ + 1)]
    pass2 = [random.choice(symbols) for _ in range(0, Symbol_ + 1)]
    pass3 = [random.choice(numbers) for _ in range(0, Number_ + 1)]
    password_list.extend(pass1 + pass2 + pass3)
    random.shuffle(password_list)
    password = ''.join(password_list)

    pass_entry.insert(0, password)

    pyperclip.copy(password)


# FINDING PASSWORD --->

def find_password():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.askokcancel(title="Oops!", message="Data file not found.")
    else:
        if website not in data:
            messagebox.askokcancel(title="Oops!", message="No details for the website exists.")
        else:
            details = data.get(website)
            messagebox.askokcancel(title=website, message=f"Email: {details['email']} \nPassword: {details['password']}")


# SAVING PASSWORD --->

def save():
    website = web_entry.get()
    email = user_entry.get()
    password = pass_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops!", message=f"PLease don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            user_entry.delete(0, END)
            user_entry.insert(END, "name@email.com")
            pass_entry.delete(0, END)


# WINDOW SETUP --->

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# logo
canvas = Canvas(width=240, height=190, highlightthickness=0)
logo = PhotoImage(file="logo_pass.png")
canvas.create_image(120, 85, image=logo)
canvas.grid(row=0, column=1)

# 1st row
web_label = Label(text="Website:", font=(FONT_NAME, 10))
web_label.grid(row=1, column=0)
web_entry = Entry(width=39)
web_entry.focus()
web_entry.grid(row=1, column=1)

search_button = Button(text="Search", bg=WHITE, font=(FONT_NAME, 9), command=find_password, highlightthickness=0, width=17)
search_button.grid(row=1, column=2)

# 2nd row
user_label = Label(text="Email/Username:", font=(FONT_NAME, 10))
user_label.grid(row=2, column=0)
user_entry = Entry(width=63)
user_entry.insert(END, "name@email.com")
user_entry.grid(row=2, column=1, columnspan=2)

# 3rd row
pass_label = Label(text="Password:", font=(FONT_NAME, 10))
pass_label.grid(row=3, column=0)
pass_entry = Entry(width=39)
pass_entry.grid(row=3, column=1)

gen_pass_button = Button(text="Generate Password", bg=WHITE, font=(FONT_NAME, 9), command=generate_password, highlightthickness=0, width=17)
gen_pass_button.grid(row=3, column=2)

# 4th row
gen_pass_button = Button(text="Add", bg=WHITE, font=(FONT_NAME, 9), command=save, highlightthickness=0, width=47)
gen_pass_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
