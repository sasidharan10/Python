ls = [1, 3, 6, 5, 4, ]

for i in ls:
    print(i, end=' ')
    if(i == 2):
        break
else:
    print("\nNumber Not Found")


"""
- Else in for loop executes only if the loop completes fully without any break,
  which is used to give the comfirmation about the loop executed successfully.
"""