import pickle

raw = {"5":"five","3":"three","4":"four","1":"one","2":"two"} 
print("Dict :",raw)

# pickling :

with open("dummyp.pkl","wb") as w:
    pickle.dump(raw,w)

# depickling :

with open("dummyp.pkl","rb") as r:
    output=pickle.load(r)
    print("Depickling :",output)

pik=pickle.dumps(raw)
# print("Pickle :",pik)

depik=pickle.loads(pik)
print("Depickle :",depik)

"""

***** Notes *****

- dumps() and loads() are for pickling and depickling variables or strings
- dump() and load() are for pickling and depickling files


"""