import json
import requests

algo = {
    'hola' : 10,
    'chau' : '11',
    'como_estas' : True,
}

print(algo) 

json_string = json.dumps(algo,indent=4)

data = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(json_string)

