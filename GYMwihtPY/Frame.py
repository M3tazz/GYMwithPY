import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Workout GUI")

# Set the window size
root.geometry("400x600")
root.configure(bg="black")

# Function to handle button clicks
def on_button_click(level):
    if level == "beginners":
        messagebox.showinfo("Selection", "ABS FOR BEGINNERS selected")
    elif level == "strength":
        messagebox.showinfo("Selection", "FOR CORE STRENGTH selected")

# Add a title label
title_label = tk.Label(root, text="DO IT FOR AFTER SELFIE", fg="white", bg="black", font=("Helvetica", 16))
title_label.pack(pady=20)

# Load images
beginners_img_path = r"Assets\anastase-maragos-4dlhin0ghOk-unsplash.jpg"  # Update with the correct path
strength_img_path = r"Assets\anastase-maragos-9dzWZQWZMdE-unsplash.jpg"  # Update with the correct path

beginners_img = Image.open(beginners_img_path)
beginners_img = beginners_img.resize((300, 200), Image.LANCZOS)
beginners_photo = ImageTk.PhotoImage(beginners_img)

strength_img = Image.open(strength_img_path)
strength_img = strength_img.resize((300, 200), Image.LANCZOS)
strength_photo = ImageTk.PhotoImage(strength_img)

# Create labels with images
beginners_img_label = tk.Label(root, image=beginners_photo, bg="black")
strength_img_label = tk.Label(root, image=strength_photo, bg="black")

# Add buttons
beginners_button = tk.Button(root, text="ABS FOR BEGINNERS", command=lambda: on_button_click("beginners"), bg="black", fg="white", font=("Helvetica", 12))
strength_button = tk.Button(root, text="FOR CORE STRENGTH", command=lambda: on_button_click("strength"), bg="black", fg="white", font=("Helvetica", 12))

# Place images and buttons
beginners_img_label.pack(pady=10)
beginners_button.pack(pady=10)
strength_img_label.pack(pady=10)
strength_button.pack(pady=10)

# Run the application
root.mainloop()
