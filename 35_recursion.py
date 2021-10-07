def factorial_recursion(n):
    if n==1:
        return n
    else:
        return n*factorial_recursion(n-1)

def factorial_iterative(n):
    fac=1
    for i in range(1,n+1):
        fac=fac*i
    return fac


def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print("Factorial (Recursive) :",factorial_recursion(5))
print("Factorial (Iterative) :",factorial_iterative(5))
print("Fibonacci (Recursive) :",fibo(6))

