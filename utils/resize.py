import cv2
from os import listdir
import argparse

# Parser
parser = argparse.ArgumentParser()
parser.add_argument("--directory", '-d', required=True, type=str, help="Pass in directory to resize")
parser.add_argument("--height", default=200, type=int)
parser.add_argument("--width", default=100, type=int)
args = parser.parse_args()

# List all file in dir
for f in listdir(args.directory):
    path = args.directory + '/' + f
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(img, (args.width, args.height))
    
    # Save result
    cv2.imwrite(path, resized)
