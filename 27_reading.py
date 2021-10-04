f=open("demo.txt","rt")
# f=open("demo.txt","rb")


# here 'f' is a file pointer which points to the file texts
# "rt" means reading in text mode (default)
 
txt=f.read()  # reading file using the pointer

# txt=f.read(6)
# readonly 6 characters

print(txt)
# print(f.readlines())

# we can even iterate the line using for loop (but dont use f.read())

# for line in f:
#     print(line)

# print(f.readline())
# print(f.readline())
# print(f.readline())

# we can even iterate the characters using for loop

# for char in txt:
#     print(char,end="")


f.close()  # always close file