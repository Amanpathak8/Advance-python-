import requests
url = "https://pokeapi.co/api/v2/pokemon"

response = requests.get(url)
#print(response) #if it is 200 then you are able to hit the data
data = response.json()
print(data)
