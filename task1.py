import tkinter as tk

def combine_inputs():
    input1 = e1.get()
    input2 = e2.get()
    input3 = e3.get()


    combined_input = input1, input2, input3

    e4.delete(0,tk.END)
    e4.insert(0,combined_input)



master = tk.Tk()

master.geometry('200x200')

l1 = tk.Label(master, text="Name:  ")
l1.pack()

e1 = tk.Entry(master)
e1.pack()

l2 = tk.Label(master,text="Student number:  ")
l2.pack()

e2 = tk.Entry(master)
e2.pack()

l3 = tk.Label(master,text="GPA:  ")
l3.pack()

e3 = tk.Entry(master)
e3.pack()

combine_button = tk.Button(master, text="Combine Inputs", command=combine_inputs)
combine_button.pack()

e4 = tk.Entry(master)
e4.pack()


master.mainloop()