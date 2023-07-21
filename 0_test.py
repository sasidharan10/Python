import http.client

conn = http.client.HTTPSConnection("covid-19-tracking.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "56bf2ba890msh46aeb5a3fd92fdfp1fa45djsnc141145c402f",
    'X-RapidAPI-Host': "covid-19-tracking.p.rapidapi.com"
}

conn.request("GET", "/v1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))