#Find the sum of all the even-valued terms in the Fibonacci sequence which do not exceed four million.

f = [1, 2]

def fib(n):
    s = 2
    i = 0
    while f[i] + f[i+1] <= n:
        f.append(f[i] + f[i+1])
        if f[i+2] % 2 == 0:
            s = s + f[i+2]
        i += 1
    return s

fib(input("not exceed n: "))
