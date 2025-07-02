n = int (input("enter a number: "))

factorial = 1

for i in range (1,n + 1):
    factorial = factorial*i

print (factorial)


def Factorial(p):
    if p == 0:
        return 1
    
    else:
        return p * factorial(p-1)