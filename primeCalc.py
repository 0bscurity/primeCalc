

# -----------------------PRIME NUMBER CALCULATOR---------------------------------------
import gui


def calc_prime(num):
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
