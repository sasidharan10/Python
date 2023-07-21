def sum1(a, b):
    """\nThis function will return the sum of given 2 no's"""  # doc string
    print("Sum :", a+b)


def avg(a, b):
    """\nThis function will return the average of given 2 no's"""
    return (a+b)/2


print(sum1.__doc__)
sum1(5, 3)
print(avg.__doc__)
print("Avg : ", avg(5, 6))  # function  with return type

"""

 doc string is the first comment of a function which gives
 us the info about the working of the function

"""

