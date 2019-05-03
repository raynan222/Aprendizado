import requests
import json


cidade = input("cidade: ")

req = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+cidade+"&appid=775a75dd27e25a869e9de335797c1c6a")

tempo = json.loads(req.text)

print("Condição:",tempo["weather"][0]["main"])
print("Descrição:", tempo["weather"][0]["description"])
print("Temperatura:",format((float(tempo["main"]["temp"])-273.15), ".1f"))

