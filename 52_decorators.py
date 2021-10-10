# we can copy a function

def f1():
    print("Copy function")

f2=f1   # f2 has a copy of f1
del f1  # deleting f1()
f2()

# we can return a function

def max_or_min(a):
    if a==1:
        return max
    else:
        return min

s=max_or_min(0)        
print(s(5,10))

# we can call a function

def exec(a):
    a("Call using print")

exec(print)

# decorators

print("\n-----Decorators------\n")

def smart_div(func):
    def inner(a,b):
        if(a<b):
            a,b=b,a
        return func(a,b)
    return inner 

@smart_div  # alternate to call decorators
def div(a,b):
    print("Div :",(a/b))

# div=smart_div(div)
div(2,5)
# OR

"""
- we use decorators to modify the existing functions, or add more functionalitites to a function
  without changing the function.

"""
