from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # Import Image and ImageTk from Pillow
from datetime import date
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect("GYMbd1.db")


def fetch_data():
    cursor = conn.cursor()
    cursor.execute("SELECT visitor_name, visitor_SSN FROM visitors")
    data = cursor.fetchall()
    print(data)
    return [f"{name} ({ssn})" for name, ssn in data]





def insert_data():
    try:
        name = name_entry.get()
        ssn = id_entry.get()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO visitors (visitor_name, visitor_SSN, dateOfDay) VALUES (?, ?, ?)",
                       (name, ssn, date_combobox.get()))
        cursor.execute("INSERT INTO BMI (visitor_id) VALUES (?)", (ssn,))
        cursor.execute("INSERT INTO calories (visitor_id) VALUES (?)", (ssn,))
        conn.commit()
        return 1

    except Exception as e:
        print("Error:", e)
        return 0

def open_system():
    # Close the current window
    if insert_data() > 0:
        root.destroy()
        import system
    else:
        # Prompt the user to enter valid data
        messagebox.showerror("ERROR", "Please enter Name and ID ")


# Call open_system() or any other relevant function to start your program

root = Tk()
root.title("Welcome Page")
root.geometry("400x600")

# Open the image using PIL and convert it for Tkinter
image_path = "Assets/background (2).png"
img = Image.open(image_path)
wel = ImageTk.PhotoImage(img)

back = Label(root, image=wel).place(relheight=1, relwidth=1)

custom_font = ("Comic Sans MS", 14, "italic")
label_one = Label(root, text="It's time to wake up the monster", font=custom_font, fg="gray", bg="#000").place(x=50,
                                                                                                               y=50)

# Labels for motivational text
eat = Label(root, text="Eat ", font=("Arial", 15), fg="gray", bg="#000").place(x=60, y=150)
dash1 = Label(root, text="-", font=("Arial", 20), fg="red", bg="#000").place(x=100, y=145)
sleep = Label(root, text="Sleep", font=("Arial", 15), fg="gray", bg="#000").place(x=120, y=150)
dash2 = Label(root, text="-", font=("Arial", 20), fg="red", bg="#000").place(x=180, y=145)
gym = Label(root, text="Gym", font=("Arial", 15), fg="gray", bg="#000").place(x=200, y=150)
dash3 = Label(root, text="-", font=("Arial", 20), fg="red", bg="#000").place(x=255, y=145)
repeat = Label(root, text="Repeat", font=("Arial", 15), fg="gray", bg="#000").place(x=280, y=150)

# Input fields

name_label = Label(root, text="Name:", font=("Arial", 15), fg="gray", bg="#000")
name_label.place(x=60, y=250)

name_entry = Entry(root, font=("Arial", 15), fg="#000", bg="#fff")
name_entry.place(x=140, y=250)

id_label = Label(root, text="ID:", font=("Arial", 15), fg="gray", bg="#000")
id_label.place(x=60, y=300)

id_entry = Entry(root, font=("Arial", 15), fg="#000", bg="#fff")
id_entry.place(x=140, y=300)

'''date_label = Label(root, text="Date : ", font=("Arial", 15), fg="gray", bg="#000").place(x=60, y=350)'''

data_label = Label(root, text="Data : ", font=("Arial", 15), fg="gray", bg="#000").place(x=60, y=350)

# Create the Combobox
date_combobox = ttk.Combobox(root)
date_combobox.place(x=140, y=350, relwidth=0.56, relheight=0.045)

# Get the current date
current_date = date.today()

# Set the Combobox value to the current date
date_combobox.set(current_date.strftime("%Y-%m-%d"))
# Fetch data from your database

'''combo_values = fetch_data()
combo_var = StringVar()
data_combobox = ttk.Combobox(root,textvariable=combo_var, values=combo_values).place(x=140, y=400, relwidth=.56, relheight=0.045)
'''
# Navigation button
btn = Button(root, text=">>>", fg="gray", font="Helvetica 15 bold", bg="#000", highlightthickness=0, bd=0,
             command=open_system)
btn.place(x=330, y=525)

root.mainloop()
#conn.close()
