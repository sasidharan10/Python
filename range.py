print("\nPrint 1 to 5 : ")
for i in range(1,6): #(start, end)
    print(i,end=" ")

print("\nPrint 5 to 1 : ")
for i in range(5,0,-1): # (start, end, decrement by) or use reversed(range(1,6))
    print(i,end=" ")

print("\nPrint 1 to 20 (Even) : ")
for i in range(0,21,2):  # (start, end, increment by)
    print(i,end=" ")