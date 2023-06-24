import os


from arg_parser import *

# Imports
from console import *
from weather import *

import numpy as np
import pandas as pd

weather = Weather()
console = Console()


def main():

    # Retrieve arguments
    args = parser.parse_args()

    days_limit = int(args.days_limit)
    console.generate_commands_table()
    if (args.helpers):
        console.generate_commands_table()

    while (True):

        break
        # pass
    # console.print([1, 2, 3])
    # console.print("[blue underline]Looks like a link")

    # text = Text.assemble(("Hello", "bold magenta"), " World!")
    # console.print(text)

    # console.print("FOO", style="white on blue")

    # table = Table(title="Star Wars Movies")

    # table.add_column("Released", justify="right", style="cyan", no_wrap=True)
    # table.add_column("Title", style="magenta")
    # table.add_column("Box Office", justify="right", style="green")

    # table.add_row("Dec 20, 2019",
    #               "Star Wars: The Rise of Skywalker", "$952,110,690")
    # table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
    # table.add_row("Dec 15, 2017",
    #               "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
    # table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

    # console = Console()
    # console.print(table)


# Define init Main function
if __name__ == "__main__":
    main()
