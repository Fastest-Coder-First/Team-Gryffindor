import os

import json
import requests

# Importing Console Custom Module
from console import *

import matplotlib.pyplot as plt

console = Console()


class WeatherAPI:
    # API URL
    API_URL = "https://api.openweathermap.org/data/2.5/weather"
    METEO_API_URL = "https://api.open-meteo.com/v1/forecast"

    def __init__(self):
        with open(os.path.join("configs", "config.json")) as f:
            self.api_key = json.load(f)['api_key']

    def get_weather_data(self, PARAMS, to_csv=False):

        PARAMS["appid"] = self.api_key

        # sending get request and saving the response as response object
        r = requests.get(url=self.API_URL, params=PARAMS)

        if (r.status_code >= 400):
            console.print_error(r.json()['message'])
            return

        # extracting data in json format
        data = dict(r.json())

        data_dict = data['weather'][0]
        data_dict['name'] = str(data['name'])
        data_dict.update(data['main'])

        # Console Display of table
        console.generate_weather_table(data_dict, to_csv)

        # Meteo API
        meteo_r = requests.get(url=self.METEO_API_URL, params={
            "latitude": data['coord']['lat'], "longitude": data['coord']['lon'], "past_days": 10, "current_weather": "true", "hourly": "temperature_2m,relativehumidity_2m,windspeed_10m"})
        self.generate_graph(dict(meteo_r.json()))

    def generate_graph(self, meteo_json):
        X = meteo_json['hourly']['time'][0:len(
            meteo_json['hourly']['time'])-1:12]
        Y = meteo_json['hourly']['temperature_2m'][0:len(
            meteo_json['hourly']['time'])-1:12]
        plt.plot(X, Y)
        plt.savefig('graph.png')
