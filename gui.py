import tkinter as tk

import primeCalc

window = tk.Tk()


def get_num():
    test_num = c_entry.get()
    return int(test_num)


c_label = tk.Label(text="Enter number to determine if it is prime")
c_entry = tk.Entry(fg="white", bg="gray", width=20)
c_button = tk.Button(window, text="Calculate", command=get_num)
a_label = tk.Label(text="")

c_label.pack()
c_entry.pack()
c_button.pack()


window.mainloop()
