l1 = [6, 2, 3, 5, 4, 1]

for i in l1:
    print(i, end=" ")


l2 = [["A", 1], ["B", 2], ["C", 3], ["D", 4], ["E", 5],]
print("")

for x, y in l2:
    print(x, ":", y)

d1 = dict(l2)
print(type(d1))

# both are correct

# for d in d1:
#     print(d,":",d1[d])

for g, h in d1.items():
    print(g, ":", h)

mx = ['a', 6, 9, "sad", "happy", 8, 6, 3, 1, 4]

for m in mx:
    if str(m).isnumeric() and m > 2:
        print(m, end=" ")
print()

# while

j = 0
while (j < 5):
    print(j, end=" ")
    j += 1
