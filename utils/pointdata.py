import requests
from config import API_KEY

first_url = 'https://api.openweathermap.org/data/2.5/weather?'


def get_weather(lat: float, lon: float):
    url = first_url + 'lat=' + str(lat) + '&lon=' + str(lon) + '&appid=' + API_KEY + '&lang=ru&units=metric'
    res = requests.get(url)
    data = res.json()
    text = f'''Локация: {data['name']}\nМаксимальная температура: {data['main']['temp_max']}°C\nСредняя температура: {data['main']['temp']}°C\nМинимальная температура: {data['main']['temp_min']}°C\nВлажность: {data['main']['humidity']}%\nДавление: {data['main']['pressure']}мм рт. ст.'''
    return text
