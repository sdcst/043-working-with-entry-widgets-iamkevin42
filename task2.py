#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""
import math
import tkinter as tk


def thehypotenuse():
    try:
        side1 = float(e1.get())
        side2 = float(e2.get())
        hypotenuse = (side1**2 + side2**2) ** 0.5
        hypotenuse_entry.delete(0, tk.END)
        hypotenuse_entry.insert(0, f"{hypotenuse:.2f}")
    except ValueError:
        print('This is invalid')


master = tk.Tk()



e1label = tk.Label(master, text='First Side: ')
e1label.grid(row=0,column=0)
e1 = tk.Entry(master)
e1.grid(row=0,column=1)



e2label= tk.Label(master, text='Second Side: ')
e2label.grid(row=1,column=0)
e2= tk.Entry(master)
e2.grid(row=1,column=1)


aa = tk.Button(master, text="Combine Inputs", command=thehypotenuse)
aa.grid(columnspan=2,row=2)


hypotenuse_label = tk.Label(master, text="Hypotenuse:")
hypotenuse_label.grid(row=3, column=0)
hypotenuse_entry = tk.Entry(master)
hypotenuse_entry.grid(row=3, column=1)

master.mainloop()