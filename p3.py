# Find the largest prime factor of a positive (composite) number

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
    return factors

pfs = prime_factors(600851475143)
largest_prime_factor = max(pfs) 
largest_prime_factor # output: 6857

# Optimize: increase factor with 2 every step

n = input("the evil big number: ")
lastFactor = 1
while n % 2 == 0:
    lastFactor = 2
    n = n / 2
if lastFactor != 2:
    lastFactor = 1
factor = 3
while n > 1:
    while n % factor == 0:
        lastFactor = factor
        n = n / factor
    factor = factor + 2
lastFactor
