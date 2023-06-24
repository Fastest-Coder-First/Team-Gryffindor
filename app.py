import os


from arg_parser import *

# Imports
from console import *
from weather import *

import rich

import numpy as np
import pandas as pd

weather = Weather()
console = Console()


def main():

    # Generate welcome message
    console.generate_welcome_message()

    # Retrieve arguments
    args = parser.parse_args()
    print(args)

    if (args.helpers == True):
        console.generate_commands_table()
        return

    weather.get_weather_data(
        PARAMS={"lat": float(args.lat), "lon": float(args.long), "city": 'london'})


# Define init Main function
if __name__ == "__main__":
    main()
