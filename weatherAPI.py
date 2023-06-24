import os

import json
import requests

# Importing Console Custom Module
from console import *

import matplotlib.pyplot as plt

# Console Instance
console = Console()

# Weather API Class


class WeatherAPI:
    # API URL
    API_URL = "https://api.openweathermap.org/data/2.5/weather"
    METEO_API_URL = "https://api.open-meteo.com/v1/forecast"

    def __init__(self):
        """
        Constructor for WeatherAPI class.
        """
        with open(os.path.join("configs", "config.json")) as f:
            self.api_key = json.load(f)['api_key']

    def get_weather_data(self, PARAMS, to_csv=False, to_graph=False):
        """
        Get Weather Data from API.

        args:
            PARAMS (dict): API Parameters
            to_csv (bool): Convert to csv
            to_graph (bool): Display Temperature Graph
        """

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
            "latitude": data['coord']['lat'], "longitude": data['coord']['lon'], "past_days": 10, "current_weather": "true", "daily": "temperature_2m_max", "timezone": "GMT", "forecast_days": 3})

        if (r.status_code >= 400):
            console.print_error(r.json()['message'])
            return

        if (to_graph):
            self.generate_graph(dict(meteo_r.json()))

    def generate_graph(self, meteo_json):
        """
        Generate Temperature Graph.

        args:
            meteo_json (dict): Meteo API JSON
        """
        X = meteo_json['daily']['time']
        Y = meteo_json['daily']['temperature_2m_max']

        # Plotting the Graph
        plt.plot(X, Y)
        plt.xticks(range(len(X)), X, rotation='vertical')
        plt.tight_layout()
        plt.savefig('graph.png')
