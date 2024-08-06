from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

root = Tk()
root.geometry('500x700')
root.title('Services')
root.resizable(False, False)

def open_bmi_page():
    subprocess.Popen(['python', 'BMI.py'])

def open_calorie_page():
    subprocess.Popen(['python', 'Calorie.py'])

def open_diet_plan_page():
    subprocess.Popen(['python', 'diet_plan_page.py'])

def open_workout_page():
    subprocess.Popen(['python', 'Workout.py'])

bg_image = Image.open(r"C:\Users\ok\Desktop\gym\background.png")
bg_photo = ImageTk.PhotoImage(bg_image, width=500, height=700)
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

bg_button1 = Button(bg_label, text='B.M.I', font=('Arial', 13), bg="black", fg='white', width=45, height=3, command=open_bmi_page)
bg_button2 = Button(bg_label, text='CALORIE', font=('Arial', 13), bg="black", fg='white', width=45, height=3, command=open_calorie_page)
bg_button3 = Button(bg_label, text='DIET PLAN', font=('Arial', 13), bg="black", fg='white', width=45, height=3, command=open_diet_plan_page)
bg_button4 = Button(bg_label, text='WORKOUTS', font=('Arial', 13), bg="black", fg='white', width=45, height=3, command=open_workout_page)

bg_button1.grid(row=0, column=0, padx=40, pady=45)
bg_button2.grid(row=1, column=0, padx=40, pady=45)
bg_button3.grid(row=2, column=0, padx=40, pady=45)
bg_button4.grid(row=3, column=0, padx=40, pady=45)

root.mainloop()
