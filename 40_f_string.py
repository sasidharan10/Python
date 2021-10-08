n = 2
str = "Good Morning"
a = "Hello, %s, %d dollars for coffee" % (str, n)
b = "Hello, {}, {} dollars for coffee".format(str, n)
c = f"Hello, {str}, {n} dollars for coffee"
print(a)
print(b)
print(c)
