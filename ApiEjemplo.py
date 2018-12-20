import json
import requests
def getData(url):
	response=requests.request("GET",url)
	if response.status_code==200:
		print("ok")
	return(json.loads(response.text))
url="https://jsonplaceholder.typicode.com/posts"
getData(url)
