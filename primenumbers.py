def FindPrime(n): #prints prime numbers
    primes = [2, 3]
    for num in range(4, n): #range definition
        notprime = False
        for p in primes:
            if num % p == 0: #checks if number is prime number
                notprime = True
        if notprime == False:
            primes.append(num)

    print (primes)

print (FindPrime(100))
