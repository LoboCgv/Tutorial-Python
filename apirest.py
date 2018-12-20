import requests
# Creamos la petición HTTP con GET:
r = requests.get("http://weather.yahooapis.com/forecastrss", params = {"w":"774508"})
# Imprimimos el resultado si el código de estado HTTP es 200 (OK):
if r.status_code == 200:
    print (r.text)