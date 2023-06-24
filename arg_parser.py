import argparse

# Parser instance
parser = argparse.ArgumentParser(description='Process some integers.')


parser.add_argument('lat', help='latitude')
parser.add_argument('long', help='longitude')
parser.add_argument('-city', help='city')
parser.add_argument('-country', help='country')
parser.add_argument('-state', help='state')
parser.add_argument(
    '--days-limit', help='Days for forecast', default=1)
