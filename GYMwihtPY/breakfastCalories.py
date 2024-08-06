from tkinter import *
import subprocess
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3



conn=sqlite3.connect("GYMbd1.db")
# Function to navigate back to system.py
def insert_data(result):

    ssn=id_entry.get()
    cursor = conn.cursor()
    cursor.execute("UPDATE calories set morning_cal=?WHERE visitor_id=?",
                   (result, ssn))

    conn.commit()
def go_back_to_system():
    root.destroy()
    subprocess.run(['python', 'system.py'])  # Assuming main() is the entry point in system.py


def CalculateBtn():
    try:
        a = int(txt1.get())
    except ValueError:
        a = 0
    try:
        b = int(txt2.get())
    except ValueError:
        b = 0
    try:
        c = int(txt3.get())
    except ValueError:
        c = 0
    try:
        d = int(txt4.get())
    except ValueError:
        d = 0
    try:
        e = int(txt5.get())
    except ValueError:
        e= 0
    try:
        f = int(txt6.get())
    except ValueError:
        f= 0
    try:
        g = int(txt7.get())
    except ValueError:
        g = 0
    try:
        h = int(txt8.get())
    except ValueError:
        h = 0
    try:
        i = int(txt9.get())
    except ValueError:
        i = 0
    total = (a * 17) +(b * 357) + (c * 112) +( d * 378) +( e * 539) + (f * 86) +(g *82)+(h*357)+(i*49)
    mess = f'The Total calories at breakfast = {total}'
    messagebox.showinfo("Total", mess)
    insert_data(total)
    return total

def resetfun():
    txt1.delete(0, END)
    txt2.delete(0, END)
    txt3.delete(0, END)
    txt4.delete(0, END)
    txt5.delete(0, END)
    txt6.delete(0, END)
    txt7.delete(0, END)
    txt8.delete(0, END)
    txt9.delete(0, END)
    id_entry.delete(0, END)
    return

root = Tk()
root.geometry('500x700')
root.title('BREAKFAST')
root.resizable(False, False)

bg_image = Image.open(r"Assets\background2.png")
bg_photo = ImageTk.PhotoImage(bg_image, width=500, height=700)
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

lbl1 = Label(bg_label, text='Cooked Egg Whites: ~17 calories', font=('Arial', 10), fg='gray', background='black')
lbl2 = Label(bg_label, text='Bacon on Biscuit: ~357 calories', font=('Arial', 10), fg='gray', background='black')
lbl3 = Label(bg_label, text='Cheese Biscuit: ~112 calories', font=('Arial', 10), fg='gray', background='black')
lbl4 = Label(bg_label, text='Egg and Bacon Biscuit: ~378 calories', font=('Arial', 10), fg='gray', background='black')
lbl5 = Label(bg_label, text='Sausage, Egg : ~539 calories', font=('Arial', 10), fg='gray', background='black')
lbl6 = Label(bg_label, text='1 Plain Pancake (4"): ~86 calories', font=('Arial', 10), fg='gray', background='black')
lbl7 = Label(bg_label, text='Pineapple: ~82 calories (1 cup chunks)         ', font=('Arial', 10), fg='gray', background='black')
lbl8 = Label(bg_label, text='Blueberries: ~84 calories (1 cup)', font=('Arial', 10), fg='gray', background='black')
lbl9 = Label(bg_label, text='Strawberries: ~49 calories (1 cup)', font=('Arial', 10), fg='gray', background='black')

txt1 = Entry(bg_label, width=30, highlightcolor='gray', highlightthickness=5, highlightbackground='gray')
txt2 = Entry(bg_label, width=30, highlightcolor='gray', highlightthickness=5, highlightbackground='gray')
txt3 = Entry(bg_label, width=30, highlightcolor='gray', highlightthickness=5, highlightbackground='gray')
txt4 = Entry(bg_label, width=30, highlightcolor='gray', highlightthickness=5, highlightbackground='gray')
txt5 = Entry(bg_label, width=30, highlightcolor='gray', highlightthickness=5, highlightbackground='gray')
txt6 = Entry(bg_label, width=30, highlightcolor='gray', highlightthickness=5, highlightbackground='gray')
txt7 = Entry(bg_label, width=30, highlightcolor='gray', highlightthickness=5, highlightbackground='gray')
txt8 = Entry(bg_label, width=30, highlightcolor='gray', highlightthickness=5, highlightbackground='gray')
txt9 = Entry(bg_label, width=30, highlightcolor='gray', highlightthickness=5, highlightbackground='gray')

id_label = Label(bg_label, text="ID:", font=("Arial", 15), fg="gray", bg="#000")
id_label.grid(row=0, column=0,padx=10, pady=10)
id_entry = Entry(bg_label, font=("Arial", 15), fg="#000", bg="#fff",width=10,highlightcolor='gray', highlightthickness=5, highlightbackground='gray')
id_entry.grid(row=0, column=1,padx=10, pady=10)

lbl1.grid(row=1, column=0, pady=10)
lbl2.grid(row=2, column=0, pady=10)
lbl3.grid(row=3, column=0, pady=10)
lbl4.grid(row=4, column=0, pady=10)
lbl5.grid(row=5, column=0, pady=10)
lbl6.grid(row=6, column=0, pady=10)
lbl7.grid(row=7, column=0, pady=10)
lbl8.grid(row=8, column=0, pady=10)
lbl9.grid(row=9, column=0, pady=10)

txt1.grid(row=1, column=1, pady=10)
txt2.grid(row=2, column=1, pady=10)
txt3.grid(row=3, column=1, pady=10)
txt4.grid(row=4, column=1, pady=10)
txt5.grid(row=5, column=1, pady=10)
txt6.grid(row=6, column=1, pady=10)
txt7.grid(row=7, column=1, pady=10)
txt8.grid(row=8, column=1, pady=10)
txt9.grid(row=9, column=1, pady=10)

btn1 = Button(bg_label, text='Total', command=CalculateBtn, width=20, height=2, background='black', fg='white', font=('Arial', 10))
btn1.grid(row=10, column=0, pady=50)
btn2 = Button(bg_label, text='Reset', command=resetfun, width=20, height=2, background='black', fg='white', font=('Arial', 10))
btn2.grid(row=10, column=1, pady=50)

# Back arrow button with command to go back to system.py
btn3 = Button(bg_label, text='<<<', font=13, background="black", foreground="gray", width=10, borderwidth=0, command=go_back_to_system)
btn3.grid(row=11, column=0, pady=10, sticky='nw', padx=10)

root.mainloop()
