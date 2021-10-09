import functools

ls=[1,2,3,4,5,6]

map_object=map(lambda x:x*x,ls)

# for i in map_object:
#     print(i,end=" ")

print(list(map_object))

"""

syntax : 

object = map(function,iterables)

- map is used to apply some changes to all elements in a list
- it will always return a object, either print the elements using a for loop or
  type-cast it into list and print

"""

obj=filter(lambda x:x>3,ls)

# for i in obj:
#     print(i,end=" ")

print(list(obj))

"""

syntax : 

object = filter(function,iterables)

- map is used to filter a list as per the given function and have only accepted items.
- it will also return a object.

"""

ans=functools.reduce(lambda x,y:x+y,ls)

print(ans)

"""

syntax : 

object = filter(function,iterables)

- reduce() helps in working with 2 items, then the resultant item is sent with next item, untill
  the list becomes into a single item.
- use functools for using this function
- used for summation, product etc.

"""


def sqr(x):
    return x*x

def cube(x):
    return x*x*x

# fucntion in a list

func=[sqr,cube]
for i in ls:
    mpj=map(lambda x:x(i),func)
    print(list(mpj))