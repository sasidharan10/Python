def fib(limit):
    a,b=0,1

    while a<=limit:
        yield a
        a,b=b,a+b
    
def factorial(n):
    fac=1
    i=1
    for i in range(1,n+1):
        fac=fac*i
        yield fac

x=fib(8)
y=factorial(5)

print("Fibonacci series : ")
for i in x:
    print(i,end=" ")

print("\nFactorial : ")
for i in y:
    print(i,end=" ")

# print(list(y)[4]) # to print the last result