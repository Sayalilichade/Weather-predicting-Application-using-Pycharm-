import requests
import json

city= input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=586a726df1c34d70967114323230209&q= {city} "

r = requests.get(url)
#print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

os.system(f"say 'the current weather in {city} is {w} degrees'")
