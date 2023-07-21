
# sets dont store elements in order(order changes) and doesnt allow duplicate elements
# sets are immutable
# sets dont have index to access elements

# converting list to set
list=[70,60,60,40,10]
s1=set(list)
print(type(s1))
print("s1 :",s1)

s2={50,30,10,50,20,40,20}
# s2.add(10)
print(type(s2))
print("s2 :",s2)

s3=s1.union(s2)  # union
s4=s1.intersection(s2)  # intersection
s5=s1.copy()     # copy
s5.clear()       # clear
print("s3 (union) :",s3)
print("s4 (intersection) :",s4)
print("s5 :",s5)
s3.remove(70)  # removes given element
s3.pop()  # removes lastly added element
print("s3 :",s3)
print(s1.isdisjoint(s2))
s3.update({1,2})
print("s3 :",s3)