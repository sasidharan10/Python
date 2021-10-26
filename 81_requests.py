import requests as r

res=r.get("https://reqres.in/api/users/2")
print("\nGet request : \n")
print("Data :",res.text)
print("Status :",res.status_code)

link="https://reqres.in/api/users"
dt={
    "name": "Neo",
    "job": "Superhuman"
}
print("\nPost request : \n")
pt=r.post(url=link,data=dt)
print("Data :",pt.text)
print("Status :",pt.status_code)