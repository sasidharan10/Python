d1 = {"arg": "messi", "nor": "haaland", "por": "fernandez",
      "fra": {"fwd": "mbappe", "mid": "pogba"}}
print("d1 :", d1)
d1["por"] = "ronaldo"
print("d1 :", d1)
var = "por"
# accessing the vaues using keys
print("d1[\"arg\"] :", d1["arg"])
print("d1[\"por\"] :", d1[var])
print("d1[\"arg\"][\"mid\"] :", d1["fra"]["mid"])

# adding new element to dictionary
# d1["bra"]="neymar"
d1.update({"bra": "neymar"})

# d2=d1 creates a pointer d2 pointing to the dictionary, so any changes done in
# one pointer gets reflected on both. therefore use d1.copy() to copy dictionary

# d2=d1
# d2["arg"]="di maria"
# print(d1)  d1 would have got changed

d2 = d1.copy()  # gets copied
d2.clear()

print("d1.keys() :", d1.keys())        # gives keys
print("d1.values() :", d1.values())    # gives values
print("d1.items() :", d1.items())      # gives keys and values

d1.pop("fra")  # item with giveen key gets deleted
d1.popitem()  # lastly added item gets deleted
print("d1 :", d1)

print(d1.get("por"))
