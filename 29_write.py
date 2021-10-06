# f=open("write.txt","w")
# f.write("Have a nice day\n")

# write "w" replaces existing text and writes the given text
# if there is no file with the given name, then it creates a new file automatically

# f=open("write.txt","a")
# f.write("Have a nice day\n")

# append "a" keeps existing text and adds the given text

f=open("write.txt","r+")
print(f.read())
a=f.write("Have a nice day\n")
print(a)

# using "r+" we can read as wel as write the files
# here "a" gives the no of characters we have written in the file