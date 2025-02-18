import requests

handle = open("key.txt")
key = handle.read()

url = f"https://api.kscope.io/v2/sec/search/MTSR?key={key}&content=sec"

payload={}
headers = {}

response = requests.get(url)

print(response.text)