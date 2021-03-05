import cv2
import argparse
import matplotlib.pyplot as plt
from os import listdir

# Parser
parser = argparse.ArgumentParser()
parser.add_argument('--image', '-i', help="Pass in image to reverse")
parser.add_argument('--write', '-w', type=bool, nargs='?', default=True, help="Save reversed image in same directory")
parser.add_argument('--display', '-d', type=bool, nargs='?', const=True, default=False, help="Display original and reversed image")
parser.add_argument('--directory', '-r', type=str, default=None, help="Loop file in directory")
args = parser.parse_args()

# Dir 
if args.directory is not None:
    for f in listdir(args.directory):
        file_full_path = args.directory + '/' + f
        img = cv2.imread(file_full_path, cv2.IMREAD_UNCHANGED)
        imgRev = (255 - img)
        newDir = args.directory + "/reversed_" + f
        cv2.imwrite(newDir, imgRev)
else:
    # Main
    imgPath = args.image
    img = cv2.imread(imgPath, cv2.IMREAD_UNCHANGED)
    imgRev = (255 - img)
    name = imgPath.split('/')[-1]
    dir = "/".join(imgPath.split('/')[:-1])

    # Write Image
    if args.write:
        newDir = dir + "/reversed_" + name
        cv2.imwrite(newDir, imgRev)
    # Display
    if args.display:
        f, ui = plt.subplots(2)
        ui[0].imshow(img)
        ui[1].imshow(imgRev)
        plt.show()