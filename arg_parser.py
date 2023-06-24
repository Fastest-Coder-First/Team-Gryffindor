import argparse
import json

import os

# Parser instance
parser = argparse.ArgumentParser(
    description='Welcome to Python Weather CLI.\n This is a command line application that helps you retrieve weather information for a particular city.')

# Load json file
with open(os.path.join("configs", "config.json")) as f:
    args_json = json.load(f)

# Adding Arguments
parser.add_argument("-helpers", action="store_true",
                    help="Display Commands")

for key, value in args_json['args'].items():
    parser.add_argument(
        key, help=value, default=10.0 if key in args_json['numeric_defaults'] else None, action="store_true" if key in args_json['bool_args'] else None)
