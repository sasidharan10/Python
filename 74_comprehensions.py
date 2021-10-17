
# list comprehension :

ls = [i for i in range(1, 11) if i % 2 == 0]
print("List : ", ls)

# Dictionary comprehension :

dc1 = {i: f"A{i}" for i in range(0, 10) if i % 2 != 0}
print("Dict : ", dc1)

dc2 = {value: key for key, value in dc1.items()}
print("Dict (reversed) : ", dc2)
# Gennrator comprehension :

gn = (i for i in range(1, 51) if i % 5 == 0)
print("Generator : ", end='')
for i in gn:
    print(i, end=" ")
