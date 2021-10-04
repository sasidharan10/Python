i = 0

while(True):
    i += 1
    if i % 2 == 0:
        continue
    if i > 10:
        break
    print(i, end=' ')
