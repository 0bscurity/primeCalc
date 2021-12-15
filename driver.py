import primeCalc

primeCalc.gui()

while 1 == 1:
    decision = input(f"Press 1 for prime calculator, and 2 to find all prime numbers: ")

    if decision == "1":
        primeCalc.calc_prime()
    elif decision == "2":
        primeCalc.prime_array()

