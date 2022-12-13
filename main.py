import requests
import json
import time
start=time.perf_counter()
def get10(name):
 url = "https://jsonplaceholder.typicode.com/todos/1/"
 response = requests.get(url=url)
 print(response, type(response))
 json_dict=response.json()
 print(json_dict)

 with open(f"files/new{name}.json", "w") as json_file:
     json.dump(json_dict, json_file)


for i in range(1,10+1):
    get10(i)
end=time.perf_counter()
print(f"elapsed:{round(end-start, 1)}")