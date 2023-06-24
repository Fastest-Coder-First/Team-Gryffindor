import os
import json

from rich.table import Table
from rich.console import Console

import pandas as pd

# Console Instance
console = Console()


class Console:

    columns = ['city', 'country', 'humidity', 'main',
               'description', 'temp', 'feels_like', 'temp_min', 'temp_max', 'pressure']

    colors = ['cyan', 'magenta', 'green', 'yellow', 'blue', 'red', 'white', 'black', 'bright_red',
              'bright_green', 'bright_yellow', 'bright_blue', 'bright_magenta', 'bright_cyan', 'bright_white']

    def __init__(self):
        # Load json file
        with open(os.path.join("configs", "texts.json")) as f:
            self.texts = json.load(f)

    def generate_welcome_message(self):
        console.print((self.texts["welcome_message"]), style="bold green")

    def generate_commands_table(self):

        table = Table(title="Weather Forecast ")

        table.add_column("S.NO",
                         style="cyan", no_wrap=True)
        table.add_column("Commands", style="magenta", justify='center')

        table.add_row("--to-csv",
                      "converts weather data to csv format")

        console.print(table)

    def generate_weather_table(self, data, to_csv=True):
        table = Table(title="Weather Forecast ")

        keys = list(filter(lambda x: x in self.columns, list(data.keys())))

        for column in keys:
            table.add_column(column,
                             style=self.colors[keys.index(column)], no_wrap=True, justify='center')

        values = [str(data[key]) for key in keys]

        # Adding Table Row
        table.add_row(values[0], values[1], values[2],
                      values[3], values[4], values[5], values[6], values[7])

        # Console Print
        console.print(table)

        if (to_csv):
            self.generate_csv(data)

    def generate_csv(self, data):
        df = pd.DataFrame(data, index=[0])
        df.to_csv('weather.csv', index=False)
