import json

with open("dummyj.json", "r") as w:
    rawdata = w.readlines()
    w.seek(0)   # taking pointer to start location
    data = json.load(w)
    # print("Rawdata :",rawdata)    # in json format
    print("Name :", data["name"])    # converted to python dict

raw = '{"5":"five","3":"three","4":"four","1":"one","2":"two"}'  # json to python

dg = '{"name":"messi","Number":"10"}'

parsed = json.loads(raw)    # for converting variables to json
print("Parsed :", parsed)
print("Parsed :", parsed['3'])


dic = {10: "Messi", 7: "Ronaldo", 9: "Lewandowski"}
print(dic)
converted = json.dumps(dic, sort_keys=1)
print(converted)


"""

***** Notes *****

- load()  =>  to convert json file to python dictionary
- loads() =>  to convert json string/variable to python dictionary
- dump()  =>  to convert python dictionary to json file  (refer 83_writing.py)
- dumps() =>  to convert python dictionary to json string 


"""
