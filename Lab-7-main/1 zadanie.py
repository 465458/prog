import requests

city_name = input("Введите город на английском языке: ")
key = input("Введите ваш API ключ с сайта OpenWeather: ")
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}")
result = response.json()
temp = result['main']['temp']
wind_speed = result['wind']['speed']
clouds = result['clouds']['all']
pressure = result['main']['pressure']

print(f"Температура: {round(temp-273.15,2)}°C\nСкорость ветра: {wind_speed}м/с\n\
Облачность: {clouds}%\nДавление: {pressure}гПа")
