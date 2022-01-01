import primeCalc

while True:
    decision = input(f"Press 1 for prime calculator, and 2 to find all prime numbers: ")

    if decision == "1":
        num = int(input("Enter a number to test: "))
        primeCalc.calc_prime(num)
    elif decision == "2":
        test_num = int(input("Enter a number to test: "))
        primeCalc.prime_array(test_num)

