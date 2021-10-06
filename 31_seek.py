f = open("demo.txt", "rt")
print(f.tell())
print(f.readline(), end="")
print(f.tell())
print(f.readline(), end="")
print(f.tell())
f.seek(0)
print(f.tell())
print(f.readline(), end="")

f.close()
# tell() returns the index at which thefile pointer is pointing to
# seek() will move the pointer to the given index
