def add1(a, b):
    return a+b


def add2(a, b): return a+b


print("Add (function) :", add1(5, 3))
print("Add (Lambda) :", add2(5, 3))

ls = [[5, 4], [1, 3], [3, 6], [7, 1]]

# sorting using 0th element and first element

ls.sort(key=lambda ls: ls[0])
print("Sort by 0th element :", ls)

ls.sort(key=lambda ls: ls[1])
print("Sort by 1st element :", ls)

"""
Syntax : 
lambda (arguments):(returning statement)

"""
