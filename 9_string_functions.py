str="have a nice day"

print("len() :",len(str))
print("count() :",str.count('a'))
print("capitalize() :",str.capitalize())
print("lower() :",str.lower())
print("upper() :",str.upper())
print("startswith() :",str.startswith('y'))
print("endswith() :",str.endswith('y'))
print("find() :",str.find('nice'))
print("replace() :",str.replace('nice',"good"))
print("isalnum() :",str.isalnum()) # no numbers
print("isalpha() :",str.isalpha()) # space does not come under alphabets
x='5'
print("isdecimal() :",x.isdecimal())
# print("center() :",str.center())
# print("find() :",str.find("nice","the"))