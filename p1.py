# Find the sum of all the multiples of 3 or 5 below 1000. 

n = input("below n: ")
s = 0
for i in range(n):
    if i%3==0 or i%5==0:
        s = s + i
print s

# Optimize

target = 999

def div(n):
    p = target//n
    return n*(p*(p+1))/2

div(3) + div(5) - div(15)
