import requests

reponse = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(reponse.json())
print(reponse.json()['title'])