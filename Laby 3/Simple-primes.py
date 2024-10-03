def if_prime(a):
    for i in range(2, a//2+1):
        if(a%i == 0):
            return False
    return True

# tu powinno być sito żeby było optymalnie ale hackerrank akceptuje czasowo też zapychacza wiec fajnie
# sito na dole

def sieve_of_erathostenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    
    for i in range(2, int(n**0.5) + 1):    #<-- od 2jki bo tamte wywalilismy do pierwiastka (można do polowy albo do calosci ale mniej optymalnie)
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

# z tym by bylo szybciej ale jest bardziej upierdliwe D:

def main():
    num = int(input())
    for i in range(2,num):
        if if_prime(i) == True:
            print(i)

main()
