from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


def show_passwords():
    show_password_window = Toplevel(window)
    show_password_window.title("All Passwords")
    show_password_window.config(padx=30, pady=30)

    website_col_label = Label(show_password_window, text="Website", font=("bold"), padx=10)
    website_col_label.grid(row=0, column=0)
    email_col_label = Label(show_password_window, text="Email/Username", font=("bold"), padx=10)
    email_col_label.grid(row=0, column=1)
    password_col_label = Label(show_password_window, text="Password", font=("bold"), padx=10)
    password_col_label.grid(row=0, column=2)

    with open("data.txt", "r") as data_file:
        data_list = data_file.readlines()

        i = 1
        for row in data_list:
            fields = row.split("|")
            website_row_label = Label(show_password_window, text=fields[0])
            website_row_label.grid(row=i, column=0)
            email_row_label = Label(show_password_window, text=fields[1])
            email_row_label.grid(row=i, column=1)
            password_row_label = Label(show_password_window, text=fields[2])
            password_row_label.grid(row=i, column=2)
            i += 1


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


def add_data():
    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get(),
        }
    }

    if len(email_entry.get()) == 0 or len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
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
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)
show_passwords_button = Button(text="Show all passwords", width=35, command=show_passwords)
show_passwords_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
