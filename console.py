import os
import json

from rich.table import Table
from rich.console import Console

# Console Instance
console = Console()


class Console:
    def __init__(self):
        # Load json file
        with open(os.path.join("configs", "texts.json")) as f:
            texts = json.load(f)

        console.print((texts["welcome_message"]), style="bold green")

    def generate_commands_table(self):

        table = Table(title="Weather Forecast ")

        table.add_column("S.NO",
                         style="cyan", no_wrap=True)
        table.add_column("Commands", style="magenta", justify='center')

        table.add_row("Dec 20, 2019",
                      "Star Wars: The Rise of Skywalker")

        console.print(table)
