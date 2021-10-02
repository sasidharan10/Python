x=5
y=10
z=4.5
name='sasidharan'
n=True

print("printing the type of data...")
print(type(x))
print(type(y))
print(type(z))
print(type(name))
print(type(n))

print("typecasting from int to string ...")
print(str(x)+str(y))

print("printing hello 5 times...")
print(5*"hello\t")
print(5*(str(x+y)+" "))

# x+y
print(x+y)
print("printing name :",name)
print("name[2] :",name[2])
print("name[-1] :",name[-1])
print("name[0:5] :",name[0:5])
print("name[4:15] :",name[4:15]) 
print("name[:10] :",name[:10])  # start is not given
print("name[4:] :",name[4:])   # end is not given
name='doll'
# name[2]='k' strings are immutable
print("name (changed) :",name)
print("len(name) :",len(name))