import os
import json

from rich.text import Text
from rich.table import Table
from rich.console import Console

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
        table.add_column("Command", style="magenta", justify='center')
        table.add_column("Box Office", justify="right", style="green")

        table.add_row("Dec 20, 2019",
                      "Star Wars: The Rise of Skywalker", "$952,110,690")

    # console = Console()
        console.print(table)
