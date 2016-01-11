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

# p2: ver.2
limit = input("not exceed n: ")
sum = 0
a = 1
b = 1
while b <= limit:
    if b%2 == 0:
        sum = sum + b
    h = a + b
    a = b
    b = h
sum

# p2: ver.2 opt. get rid of the testing for even values 
limit = input("not exceed n: ")
sum = 0
a = 1
b = 1
c = a + b
while c < limit:
    sum = sum + c
    a = b + c
    b = c + a
    c = a + b
sum

# E(n)=4*E(n-1)+E(n-2)
# F(n)=4*F(n-3)+F(n-6)
