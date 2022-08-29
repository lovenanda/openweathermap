
import requests, json

apiKey = "ad1b9daf7b80abf7c3e0093d81a22d13"

kota = input("masukan daerah : ")

base_url = "http://api.openweathermap.org/data/2.5/weather?"

url_get = base_url +"appid=" + apiKey + "&q=" + kota

weather_data = requests.get(url_get).json()

temperatur = weather_data["main"]["temp"] - 273.15

deskripsi = weather_data["weather"][0]["description"]

lokasi = weather_data["name"]

print(lokasi)
print("Temperatur = "+ str(round(temperatur)))
print(deskripsi)

