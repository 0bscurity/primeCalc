# -----------------------PRIME NUMBER CALCULATOR---------------------------------------


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


def prime_array(test_num):
    primelist = []

    for i in range(2, test_num + 1, 2):
        if all(i % j != 0 for j in range(3, int(i**.5) + 1, 2)):
            primelist.append(i)

    print(primelist)
