import tkinter as tk

# -----------------------Command Line---------------------------------------


def calc_prime():
    num = int(input("Enter number to check if prime: "))
    f = False

    for i in range(2, num):
        if (num % i) == 0:
            f = True
            break

    if f:
        print(f"{num} is not prime")
    else:
        print(f"{num} is prime")


def prime_array():
    primelist = []

    for number in range(2, 101):
        prime = True
        for j in range(2, number):
            if number % j == 0:
                prime = False
        if prime:
            primelist.append(number)

    print(primelist)


# -------------------------------------------------------------------------


def gui():
    window = tk.Tk()

    c_label = tk.Label(text="Enter number to determine if it is prime")
    c_entry = tk.Entry(fg="white", bg="gray", width=20)
    c_button = tk.Button(text="Calculate")

    c_label.pack()
    c_entry.pack()
    c_button.pack()

    test_num = c_entry.get()

    window.mainloop()

    return test_num
