from math import sqrt

def find_unique_primes(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    n = str(n)
    primes = set()
    
    for i in range(1, len(n) + 1):
        for j in range(len(n) - i + 1):
            num = int(n[j:j + i])
            if is_prime(num):
                primes.add(num)
    
    primes = sorted(primes, key=lambda x: str(x), reverse=True)
    
    for k in primes:
        print(k)
find_unique_primes(input())
