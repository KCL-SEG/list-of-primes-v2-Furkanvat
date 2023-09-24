"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    
    list = []
    counter = 2
    def isPrime(n):
        if n == 1:
            return True
        for i in range(2,n):
            if (n % i) == 0:
                return False
        
        return True
            
    while len(list) < number_of_primes:
        if isPrime(counter):
            list.append(counter)
        counter += 1

    return list
