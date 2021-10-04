tup=(2,4,6,8)
print(tup)
print(tup[0])
# tup[0]=1 immutable
print("count(8) : ",tup.count(8))
print("index(8) : ",tup.index(8))

#for making single element in tuple ',' should be added after the element to indicate it is a tuple
tup2=(10,)
print(tup2) 
"""
this is a multi line comment

tuples are immutable while lists are mutable
Accessing elements in tuples is faster compared to lists as elements are immutable

"""

#set

set={4,3,2,1,3,2}
print(set)
# set[0]=3 immutable
set.add(6)
set.add(5)
set.pop()
set.remove(6)
print(set)