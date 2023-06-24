import os
import json

from rich.table import Table
from rich.console import Console

import pandas as pd

# Console Instance
console = Console()


class Console:

    columns = ['name', 'country', 'humidity', 'main',
               'description', 'temp', 'feels_like', 'temp_min', 'temp_max', 'pressure']
    
    weather_icons = {
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌫",
    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌫"
}

    colors = ['cyan', 'magenta', 'green', 'yellow', 'blue',
              'red', 'bright_magenta', 'bright_green', 'bright_red']

    commands = {'--to-csv': 'Converts Weather Data to csv format',
                '--temp-graph': 'Display Temperature Graph'}

    def __init__(self):
        # Load json file
        with open(os.path.join("configs", "texts.json")) as f:
            self.texts = json.load(f)

    def generate_welcome_message(self):
        console.print((self.texts["welcome_message"]), style="bold green")

    def generate_commands_table(self):
        """Creation of helpers table.
    
        """

        table = Table(title="Commands Table ")

        table.add_column("S.NO",
                         style="cyan", no_wrap=True)
        table.add_column("Commands", style="magenta", justify='left')
        table.add_column("Description", style="green", justify='left')

        for inx, key in enumerate(self.commands):
            table.add_row(
                str(inx+1), key, self.commands[key])

        console.print(table)

    def generate_weather_table(self, data, to_csv=True):
        """
        Creation of weather table.
        
        args:
            data (dict): Weather Data
            to_csv (bool): Convert to csv   
        """

        table = Table(title="Weather Forecast - " + data['name'])

        keys = list(filter(lambda x: x in self.columns, list(data.keys())))

        for column in keys:
            table.add_column(column,
                             style=self.colors[keys.index(column)], no_wrap=True, justify='center')

        # Type Casting
        values = [str(data[key]) for key in keys]

        # Adding Table Row
        table.add_row(values[0], values[1] +  self.weather_icons[data['icon']], values[2],
                      values[3], values[4], values[5], values[6], values[7], values[8])

        # Console Print
        console.print(table)

        if (to_csv):
            self.generate_csv(data)

    def print_error(self, error_msg):
        """
        Prints error message in red color.

        args:
            error_msg (str): Error Message
        """
        console.print("Error : " + error_msg, style="bold red")

    def generate_csv(self, data):
        """
        Generates csv file from weather data.

        args:
            data (dict): Weather Data
        """    
        pd.DataFrame(data, index=[0]).to_csv('weather.csv', index=False)
