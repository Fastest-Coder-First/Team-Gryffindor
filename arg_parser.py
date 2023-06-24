import argparse

# Parser instance
parser = argparse.ArgumentParser(
    description='Welcome to Python Weather CLI.\n This is a command line application that helps you retrieve weather information for a particular city.')


parser.add_argument('lat', help='latitude')
parser.add_argument('long', help='longitude')
parser.add_argument("-helpers", action="store_true",
                    help="Display Commands")

parser.add_argument('-city', help='city')
parser.add_argument('-country', help='country')
parser.add_argument('-state', help='state')
parser.add_argument("--to-csv", action="store_true",
                    help="converts weather data to csv format")
parser.add_argument(
    '--days-limit', help='Days for forecast', default=1)
