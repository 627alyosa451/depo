def prime_checker(number):
    is_prime = True
    for _ in range(2, number):
        if number % _ == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number")
        
n = int(input("Check this number: "))
prime_checker(number=n)
