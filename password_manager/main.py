from tkinter import *
import json
from tkinter.messagebox import showerror, showinfo
import string
import secrets



DB_FILENAME = "db.json"

def generate_password():
    #xxxx-xxxx-xxxx
    length= 12
    chars = string.ascii_letters + string.digits + string.punctuation
    secure_password = "".join([secrets.choice(chars) for _ in range(length)])
    print(secure_password)
    pass_entry.insert(0,secure_password)

def search_password():
    website = web_entry.get()
    database = load_file(DB_FILENAME)
    
    try:
        user_data = database[website]
        email = user_data["email"]
        password = user_data["password"]

        # Show success message with the found credentials
        showinfo(title=f"{website}", message=f"User: {email}\nPassword: {password}")

    except KeyError:
        return showerror(title="Error", message=f"{website} does not exist!")

def load_file(file):

    try:
        with open(file, "r") as f:
            data = json.load(f)
        
    except FileNotFoundError:
        return {}
    
    return data

def save_file(data, database):
    with open(database, "w") as f:
        json.dump(data, f, indent=4)

def add_password():
    website= web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()


    if not website or not email or not password:
        showerror(title="Error", message="Please fill all fiels")
        return
    
    database = load_file(DB_FILENAME)

    database[website] = {
        "email":email,
        "password":password    
    }

    save_file(database, DB_FILENAME)
    showinfo(title="Success", message="Password added successfully!")

    web_entry.delete(0,END)
    pass_entry.delete(0,END)


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)



canvas = Canvas(height=256, width=256)
logo = PhotoImage(file="lock.png")
canvas.create_image(128,128, image = logo)
canvas.grid(row=0, column=1, columnspan=3)

web_lbl = Label(text="Web: ")
web_lbl.grid(row=1, column=0)

web_entry = Entry(width=27)
web_entry.grid(row=1, column=1)
web_btn_search = Button(text="Search", width=10, command=search_password)
web_btn_search.grid(row=1, column=2)

email_lbl = Label(text="Email: ")
email_lbl.grid(row=2, column=0)
email_entry = Entry(width=42)
email_entry.grid(row=2, column=1, columnspan=2)

pass_lbl = Label(text="Password: ")
pass_lbl.grid(row=3, column=0)

pass_entry = Entry(width=27)
pass_entry.grid(row=3, column=1)

pass_generator = Button(text="Generator", width=10, command=generate_password)
pass_generator.grid(row=3, column=2)

add_btn = Button(text="Add", width=45, command=add_password)
add_btn.grid(row=4, column=0, columnspan=3)






window.mainloop()