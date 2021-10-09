def print1(a,b,c,*ls):
    print(type(ls))
    print(a,b,c,end=":")
    for i in ls:
        print(i,end=" ")

def print2(a,b,**map):
    print(type(map))
    print(a,b)
    for key,val in map.items():
        print(key,":",val)


print1(1,2,3,6,5,4)
print("\n")
print2(56,96,PSG=1,BAR=2,BD=3,FCB=4,TOT=5)

"""
- *args is used to get arguments when there is no definite limit of no of arguments
- we can send a function without any agruments also, it will work
- In func definition, the first occuring parameters will have their respective arguments and
  the remainign will be received by the *args tuple
- *args is always received as a tuple meanwhile kwargs receives in dictionary
- Syntax : func(normal,*args,**kwargs) 
- **kwargs is to receive key, value paris in the arguments

"""