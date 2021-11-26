import argparse
from recomender import recomender

parser = argparse.ArgumentParser(description='Recomend.')
parser.add_argument('file',
                    help='Load the file')

args = parser.parse_args()

rec = recomender(args.file)
rec.euclidea()
