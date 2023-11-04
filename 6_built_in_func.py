import math
x = 10
y = 5.678
z = -25

print("abs() :", abs(z))
print("round() :", round(y))
print("round(5.2) :", round(5.2))
print("round(5.5) :", round(5.5))
print("round(5.8) :", round(5.8))
print("math.ceil() :", math.ceil(y))
print("math.floor() :", math.floor(y))
print("math.pi :", math.pi)
print("round() :", round(y))
print("max() :", max(x, y))
print("min() :", min(x, y))
a = [3, 6, 2, 7, 9]
b = [3, 6, 2, 7, 9, 5, 8, 1, 4]
print(a)
print("sum() :", sum(a))
print("sorted() :", sorted(a))
g = slice(0, 3)
h = slice(0, 9, 2)  # slice(start, end, step)
print("slice() :", a[g])
print("slice() :", b[h])
