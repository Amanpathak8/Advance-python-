import requests
url = "https://pokeapi.co/api/v2/pokemon"

response = requests.get(url)
#print(response) #if it is 200 then you are able to hit the data
total_record = response.json().get("count")
print(total_record)

#in website we have so many query paramters like offset = 20 and limit 20 is its set by api builder not us 
# so it will send 20 data at one point of time beacuse likmit is 20  in one call then wwe have to querty data agin with
# new offset with 20-40 so we have to set the parameter by using for loop s
all_data = []
for i in range(0,total_record,20):
    paginated_url = f"{url}?offset ={i}&limit= 20"
    response = requests.get(paginated_url)
    data = response.json()
    all_data.append(data)  # you can use extent too 
    
print(len(all_data))
   
    