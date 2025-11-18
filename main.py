from tkinter import *
from tkinter import messagebox
import os
import random
# Password Generater

#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list= [random.choice(letters) for _ in range(nr_letters)]

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

# Get folder where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "data.txt")  # This is the full path for your file

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    print("Save function called!")  # debug

    website = web_Entry.get()
    email = email_Entry.get()
    password = pass_Entry.get()
    
    is_ok = messagebox.askokcancel(title=website, message=f"these are the details entered: \nEmail:{email} \n password: {password}.\n is it okay to save")
    
    if not website or not password:
        messagebox.showinfo(title="Oops",message="The Bracets Are empty")
    else:
        if is_ok:
            with open(file_path, "a", encoding="utf-8") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                print(f"Saved: {website} | {email} | {password}")  # debug
                web_Entry.delete(0, END)
                pass_Entry.delete(0, END)
   

# ---------------------------- TKINTER LAYOUT ------------------------------- #

# Canvas / Image
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file=r"E:\Python programming\python_100D_course\Day29\password-manager-start\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
web_label = Label(text="Website")
web_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password")
pass_label.grid(row=3, column=0)

# Entries
web_Entry = Entry(width=35)
web_Entry.grid(row=1, column=1, columnspan=2)
web_Entry.focus()
email_Entry = Entry(width=35)
email_Entry.grid(row=2, column=1, columnspan=2)
email_Entry.insert(0, "enterurownmail")
pass_Entry = Entry(width=21)
pass_Entry.grid(row=3, column=1)

# Buttons
generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(row=3, column=2)
add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
