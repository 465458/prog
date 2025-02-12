import requests
import random

key = input("Введите ваш API ключ с КиноПоиска: ")
genre = input("Введите желаемый жанр: ")

headers = {"X-API-KEY": key}
result = requests.get(f"https://api.kinopoisk.dev/v1.2/movie/search?keyword={genre}", headers=headers)

data = result.json()

movie = random.choice(data["docs"])
name = movie['name']
rating = movie['rating']
geners = movie['genres']
description = movie['description']
year = movie['year']
countries = movie['countries']
movieLength = movie['movieLength']
print(f"Название фильма: {name}\nРэйтинг: {rating}\nЖанры: {geners}\nОписание: {description}\n\
Год выпуска: {year}\nСтрана производства: {countries}\nДлительность: {movieLength} мин\n")
