def reing(low,up): # range() ma che funziona veramente mannaggiasantantonio
    out = []
    i = low
    while i <= up:
        out.append(i)
        i += 1
    return out

def primes_until_n (upper_limit):
    #crivello di eratostene. prima annulla tutti i multipli di numeri diversi da 0 e 1 (lel), poi raccoglie i rimanenti primi 
    numbers = reing(1,upper_limit)
    for numb in numbers:
        if numb != 0 and numb != 1:
            to_remov = 2*numb
            while to_remov <= upper_limit:
                numbers[to_remov-1] = 0
                to_remov += numb
    primes = []
    for prim in numbers:
        if prim != 0:
            primes.append(prim)
    primes.remove(1)
    return primes

def factorize_n(n): # forza bruta. occhio che ti fotte l'esistenza
    primes = primes_until_n(n**0.5 + 1)
    factors = []
    for prime in primes:
        if n % prime == 0:
            factors.append(prime)
            n = n/prime # ottimizzazione grezza
    return factors

def fibonacci_until_n(n): # lol
    out = [1,1]
    for i in reing(2,n):
        out.append(out[i-2]+out[i-1])
    return out

def even_from_list(liste):
    out = []
    for elem in liste:
        if elem % 2 == 0:
            out.append(elem)
    return out

def odd_from_list(liste):
    out = []
    for elem in liste:
        if elem % 2 == 1:
            out.append(elem)
    return out

def palyndrome_check(n):
    if str(n) == str(n)[::-1]:
        return 1
    else:
        return 0

def number_in_digits(n): # scompone un intero in una lista delle sue cifre
    numbo = list(str(n))
    digits = []
    for cifra in numbo:
        digits.append(int(cifra))
    return digits

def pythagorean_triplets_until_n(n): # esatto
    triplets = []
    for i in reing(1,n):
        for j in reing (i,n):
            for k in reing(j,n):
                if i**2 + j**2 == k**2:
                    triplets.append([i,j,k])
    return triplets

def list_sum(liste): #tutta la lista
    summ = 0
    for i in liste:
        summ = summ + i
    return summ


