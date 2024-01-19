from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = ""

    total_length = nr_letters + nr_numbers + nr_symbols

    numberlen = 0
    letterlen = 0
    symbollen = 0
    i = 0

    while i < total_length:
        randomnum = random.randint(0, 2)
        if randomnum == 0:
            if letterlen < nr_letters:
                password_letter = password_letter + letters[random.randint(0, len(letters) - 1)].lower()
                letterlen += 1
                i += 1
        if randomnum == 1:
            if numberlen < nr_numbers:
                password_letter = password_letter + numbers[random.randint(0, len(numbers) - 1)]
                numberlen += 1
                i += 1
        if randomnum == 2:
            if symbollen < nr_symbols:
                password_letter = password_letter + symbols[random.randint(0, len(symbols) - 1)]
                symbollen += 1
                i += 1

    password_input.insert(0, password_letter)
    pyperclip.copy(password_letter)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website_name = website_name_input.get().title()
    email = email_username_input.get()
    password = password_input.get()
    new_dist = {
        website_name: {
            "email": email,
            "password": password
        }
    }
    if len(website_name) < 1 or len(password) < 1:
        messagebox.showerror(title="Oops", message="dont leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"do you want to save\nwebsite: {website_name}\nemail: {email}\npassword: {password}")

        if is_ok:
            try:
                with open("data.json", mode="r") as f:
                    # reading old data inside file
                    data = json.load(f)
                    # updating the file with new data
                    data.update(new_dist)
            except FileNotFoundError:
                with open("data.json", mode="w") as f:
                    json.dump(new_dist, f, indent=4)

            else:
                with open("data.json", mode="w") as f:
                    json.dump(data, f, indent=4)

            finally:
                website_name_input.delete(0, END)
                password_input.delete(0, END)

# ----------------------------- Find password ----------------------------

def find_password():
    website_name = website_name_input.get().title()
    try:
        with open("data.json", mode="r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="File not found", message="There is no data file")
    else:
        try:
            details = data[website_name]
            messagebox.showinfo(title=website_name, message=f"Email: {details['email']}\n Password: {details['password']}")
        except KeyError:
            messagebox.showinfo(title="Not found", message=f"No data of {website_name}")
    finally:
        website_name_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #]


window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_name_text = Label(text="Website:")
website_name_text.grid(row=1, column=0, sticky="e")

website_name_input = Entry(width=24)
website_name_input.grid(row=1, column=1,sticky="e")
website_name_input.focus()

search_btn = Button(text="search", width=10, command=find_password)
search_btn.grid(row=1, column=2, sticky="w")

email_username_text = Label(text="Email/Username:")
email_username_text.grid(row=2, column=0, sticky="e")

email_username_input = Entry(width=42)
email_username_input.grid(row=2, column=1, columnspan=2, sticky="e")
email_username_input.insert(0, "mohankumarhr2003@gmail.com")

password_text = Label(text="Password:")
password_text.grid(row=3, column=0, sticky="e")

password_input = Entry(width=24)
password_input.grid(row=3, column=1, sticky="e")

generate_pass_btn = Button(text="Generate password", command=password_generator)
generate_pass_btn.grid(row=3, column=2, sticky="w")

add_btn = Button(text="Add", width=36, command=save_data)
add_btn.grid(row=5, column=1, columnspan=2, sticky="e")

window.mainloop()
