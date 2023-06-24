import os

import json
import requests

# Importing Console Custom Module
from console import *


console = Console()


class Weather:
    API_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self):
        with open(os.path.join("configs", "config.json")) as f:
            self.api_key = json.load(f)['api_key']

    def get_weather_data(self, PARAMS):

        PARAMS["appid"] = self.api_key

        # sending get request and saving the response as response object
        r = requests.get(url=self.API_URL, params=PARAMS)

        # extracting data in json format
        data = dict(r.json())

        data_dict = data['weather'][0]
        data_dict.update(data['main'])

        # Console Display of table
        console.generate_weather_table(data_dict)
