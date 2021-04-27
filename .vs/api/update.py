import requests
import json
import base64
import time

response = requests.get('http://dataservice.accuweather.com/currentconditions/v1/2807435?apikey=kaGDbpVPVB7jYAATABechNo85ZcGApy7')
x = response.json()
y = json.dumps(x)
z = json.loads(y)
var = z[0]['HasPrecipitation']
precipitation = str(var)
c_temp = str(z[0]["Temperature"]["Metric"]["Value"])
weather = z[0]["WeatherText"]
while (1>0):
    
    with open("weather.json", "w") as write_file:
        json.dump(z, write_file)

    file = open("data.txt","w")

    file.write("Temperature:\n"+c_temp+"\nWeather:\n"+weather)

    file.close()

    print("Changed")

    time.sleep(600)
