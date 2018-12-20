# API KEY 9Opxu6V5CDy1pyw8i8h0MTQ7vGnAT004EO5FiGLr
#https://api.nasa.gov/neo/rest/v1/feed?start_date=2018-12-18&end_date=2018-12-19&api_key=9Opxu6V5CDy1pyw8i8h0MTQ7vGnAT004EO5FiGLr
#https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=9Opxu6V5CDy1pyw8i8h0MTQ7vGnAT004EO5FiGLr

'''
sol	int	none	sol (ranges from 0 to max found in endpoint)
camera	string	all	see table above for abbreviations
page	int	1	25 items per page returned
api_key	string	DEMO_KEY	api.nasa.gov key for expanded usage
'''
import json
import requests
from itertools import groupby
import flask


def request(url,api_key="9Opxu6V5CDy1pyw8i8h0MTQ7vGnAT004EO5FiGLr"):
	url+="?sol=1000&api_key="+api_key
	response=requests.request("GET",url)
	if response.status_code==200:
		print("ok")
	else:
		print(response.status_code)
	return(json.loads(response.text))


	
def build_web_page(diccionario):
	if(len(diccionario)>0):
		html="<html>\n<head>\n</head>\n<body>\n<ul>"
		for data in diccionario["photos"]:
			html+='\n<li><img src="{}"></li>'.format(data["img_src"])
		f=open("pagina.html","w")
		f.write(html)
		f.close()
		html+='</ul>\n</body></html>'
		return html
	else:
		print("No hay elementos")

def photos_count(data):
	lista=[]
	for dato in data:
		lista.append(dato["camera"]["name"])
	lista.sort()
	salida= {k: len(list(v)) for k, v in groupby(lista)}
	return(salida)
#	print(data[0]["camera"]["name"])
	#total_photos


#build_web_page(data)
#print(photos_count(data["photos"]))

app = flask.Flask(__name__)
app.config["DEBUG"] = True
url="https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
data=request(url)

@app.route('/', methods=['GET'])
def home():
	return build_web_page(data)
	
app.run()
    