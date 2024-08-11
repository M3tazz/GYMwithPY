import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def calculate_total():
    total = 0
    for entry in entries:
        try:
            total += int(entry.get())
        except ValueError:
            pass
    total_label.config(text=f"Total: {total} cal")

root = tk.Tk()
root.title("Calorie Counter")
root.geometry("400x600")

# Load the background image
image_path = r"Assets\F1.jpg"
image = Image.open(image_path)
image = image.resize((400, 600), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame for the food items
list_frame = ttk.Frame(root, style="Custom.TFrame")
list_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

food_items = [
    ("Plain Cooked Rice (1.0 bowl)", 173),
    ("Toor Dal (1.0 bowl)", 134),
    ("Chapati (2.0 piece)", 97),
    ("Curd Rice (1.0 bowl)", 176),
    ("Mixed Vegetables (1.0 bowl)", 82),
    ("Sauteed Vegetables (1.0 bowl)", 82),
    ("Sambar (1.0 bowl)", 83),
    ("Masoor Dal (1.0 bowl)", 132),
    ("Chicken Curry (1.0 bowl)", 359),
    ("Moong Dal (1.0 bowl)", 342)
]

entries = []
for i, (food, cal) in enumerate(food_items):
    food_label = ttk.Label(list_frame, text=f"{food} : {cal} cal", style="Custom.TLabel")
    food_label.grid(row=i, column=0, sticky="W", pady=2)
    entry = ttk.Entry(list_frame, width=5)
    entry.grid(row=i, column=1, padx=5)
    entries.append(entry)

total_button = ttk.Button(list_frame, text="Total", command=calculate_total)
total_button.grid(row=len(food_items), column=0, pady=10)

total_label = ttk.Label(list_frame, text="Total: 0 cal", style="Custom.TLabel")
total_label.grid(row=len(food_items), column=1, pady=10)

def reset_entries():
    for entry in entries:
        entry.delete(0, tk.END)
    total_label.config(text="Total: 0 cal")

reset_button = ttk.Button(list_frame, text="Reset", command=reset_entries)
reset_button.grid(row=len(food_items) + 1, column=0, pady=5)

root.mainloop()
