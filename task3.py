"""
Create the interface shown.  The program should be able to perform the math operation specified
by the buttons and display the entry in the 3rd entry widget;
"""
import tkinter as tk

w = tk.Tk()
w.title("Simple Calculator")

def operations(operation):
    num1 = float(e[0].get())
    num2 = float(e[1].get())
    try:
        if operation == "+":
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == 'x':
            result = num1 * num2
        elif operation == '÷':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        e[2].config(state='normal')
        e[2].delete(0, tk.END)
        e[2].insert(0, result)
    except ValueError:
        e[2].delete(0, tk.END)
        e[2].insert(0, "Invalid input")
    except ZeroDivisionError:
        e[2].delete(0, tk.END)
        e[2].insert(0, "Cannot divide by zero")
    finally:
        e[2].config(state='disabled')

l = []
l.append(tk.Label(w, text="Number 1"))
l.append(tk.Label(w, text="Number 2"))
l.append(tk.Label(w, text="Calculator Result"))

e = []
e.append(tk.Entry(w))
e.append(tk.Entry(w))
e.append(tk.Entry(w, state='disabled'))

b = []
b.append(tk.Button(w, text="+", command=lambda: operations("+")))
b.append(tk.Button(w, text="-", command=lambda: operations("-")))
b.append(tk.Button(w, text="x", command=lambda: operations("x")))
b.append(tk.Button(w, text="÷", command=lambda: operations("÷")))


l[0].grid(row=0, column=0, columnspan=2)
l[1].grid(row=0, column=2, columnspan=2)
l[2].grid(row=1, column=0, columnspan=4)
e[0].grid(row=2, column=0, columnspan=2)
e[1].grid(row=2, column=2, columnspan=2)
b[0].grid(row=3, column=0)
b[1].grid(row=3, column=1)
b[2].grid(row=3, column=2)
b[3].grid(row=3, column=3)
e[2].grid(row=4, column=0, columnspan=4)

w.mainloop()
