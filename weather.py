import json
import requests


class Weather:
    API_URL = "https://api.openweathermap.org/data/3.0/onecall?"

    def __init__(self): pass

    def get_weather_data(self, params):
        # defining a params dict for the parameters to be sent to the API
        PARAMS = params

        # sending get request and saving the response as response object
        r = requests.get(url=self.API_URL, params=PARAMS)

        # extracting data in json format
        data = r.json()

        print(data)
