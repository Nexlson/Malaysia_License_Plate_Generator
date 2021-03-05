from fake_plate_generator import Generator
import argparse
import os

'''
Parameters for generators:
1. state (string) = The first alphabets for car plate based on state and territory, must enter full state name 
Example: 
    "Perak": "A", "Selangor": "B", "Pahang": "C", "Kelantan": "D", "Putrajaya": "F", 
    "Johor": "J", "Kedah": "K", "Malacca": "M", "Negeri Sembilan": "N", "Penang": "P",
    "Perlis": "R", "Kuala Lumpur(1)": "W", "Kuala Lumpur(2)": "V", "Sarawak": "Q", "Sabah": "S"

2. plate_type (string) = The type of plate
Example: 
    "single", "double"

3. variant_plate (boolean) = add a random alphabet at back

4. total_plate (integer) = number of plate generated

5. alphabet_num (integer) = number of alphabet in plate (1 - 3)

6. number_num (integer) = number of numerical number in plate (1 -4)

7. font_type (string) =
Example:
    "Arial_Bold", "Charles_Wright

8. display (boolean) = display result

'''

# parser 
parser = argparse.ArgumentParser()
parser.add_argument("--plate_type", type=str, help="type of plate. Eg: 'single', 'double'", default="single")
parser.add_argument("--total_plate", required=True, type=int, help="number of plate generated")
parser.add_argument("--variant", type=bool, default=False, help="add a random alphabet at back")
parser.add_argument("--state", type=str, default="Penang", help=
    "The first alphabets for car plate based on state and territory, must enter full state name Example: 'Perak': 'A', 'Selangor': 'B', 'Pahang': 'C', 'Kelantan': 'D', 'Putrajaya': 'F', 'Johor': 'J', 'Kedah': 'K', 'Malacca': 'M', 'Negeri Sembilan': 'N', 'Penang': 'P', 'Perlis': 'R', 'Kuala Lumpur(1)': 'W', 'Kuala Lumpur(2)': 'V', 'Sarawak': 'Q', 'Sabah': 'S'")
parser.add_argument("--alphabet_num", type=int, default=3, help="number of alphabet in plate (1 - 3)")
parser.add_argument("--number_num", type=int, default=4, help="number of numerical number in plate (1 -4)")
parser.add_argument("--font_type", type=str, default="Arial_Bold", help="The font type. There are 'Arial_Bold', 'Charles_Wright'")
parser.add_argument("--display", type=bool, default=False, help="display result")
args = parser.parse_args()

# Main
cwd = os.getcwd()
destination = cwd + '/data/generated_plates'
# Create directory if not exist
if not os.path.exists(destination):
    os.mkdir(destination)
gen = Generator()
gen.generatePlates(args.plate_type, args.total_plate, args.variant, args.state, args.alphabet_num, args.number_num, args.font_type, args.display)