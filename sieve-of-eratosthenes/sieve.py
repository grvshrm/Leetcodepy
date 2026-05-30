import math

def primes_upto(n):
    sieve = [True] * (n + 1)

    sieve[0] = sieve[1] = False

    for i in range(2, math.isqrt(n) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False

    return [i for i in range(n+1) if sieve[i]]

print(primes_upto(100))