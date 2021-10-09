ls=["psg","fcb","mu","mc","tot","bor"]

for index,item in enumerate(ls):
    print(f"{index} : {item}")
print()
for i,t in enumerate(ls):
    if i%2==0:
        print(i,":",t)