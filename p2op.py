f = [1, 2]

def fib(n):
    i = 0
    while f[i] + f[i+1] <= n:
        f.append(f[i] + f[i+1])
        i += 1    
    return f

fib(input("not exceed n: "))

even = [x for x in f if x%2 == 0]
sum(even)
