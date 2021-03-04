import cv2 
import os
import random
import logging

class Generator():
    def __init__(self, plate_type="single", total_plate=10, variant_plate=False ,state="Penang", alphabet_num=3, number_num=4):
        self.plate_type = plate_type
        self.state = state
        self.number_count = number_num
        self.alpha_count = alphabet_num
        self.total_plate = total_plate
        self.variant_plate = variant_plate

    def getCharPath(self, alphabet, font):
        path = str(os.getcwd()) + '/data/{}/reversed/alphabets/{}.png'.format(font, alphabet)
        return path
    
    def getRandomPlate(self, stateName, front_alpha_num, num_num, variant):
        # Constant
        state = {"Perak": "A", "Selangor": "B", "Pahang": "C", "Kelantan": "D", "Putrajaya": "F", 
        "Johor": "J", "Kedah": "K", "Malacca": "M", "Negeri Sembilan": "N", "Penang": "P",
        "Perlis": "R", "Kuala Lumpur(1)": "W", "Kuala Lumpur(2)": "V", "Sarawak": "Q", "Sabah": "S"}
        alphabets_number = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q",
        "R", "S", "T", "U", "V", "W", "X", "Y"]
        first_num = ["1","2","3","4","5","6","7","8","9"]
        other_num = ["0","1","2","3","4","5","6","7","8","9"]
        # Variables
        firstNum = random.choice(first_num)
        alphabets_group = state[stateName]
        number_group = firstNum
        # First alpha is set to be state so minus 1
        for x in range(front_alpha_num- 1):
            alphabets_group += random.choice(alphabets_number)
        # First number is set so minus 1
        for y in range(num_num - 1):
            number_group += random.choice(other_num)
        plate = alphabets_group + number_group
        # Add a single alphabets at last
        if variant:
            last_alpha = random.choice(alphabets_number)
            plate += last_alpha
        return plate

    def readImage(self, imgPath):
        img = cv2.imread(imgPath)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img


    def generatePlates(self):
        # Import plate type
        plate_path = str(os.getcwd()) + '/data/backplate/'
        if self.plate_type == "single":
            name = 'single_line_backplate.jpg'
            back_plate = self.readImage(plate_path+name)
        elif self.plate_type == "double":
            name = 'double_line_backplate.jpg'
            back_plate = self.readImage(plate_path+name)
        else:
            return logging.error("Please specify the plate type")
        # Generate random car plate
        plate_number = self.getRandomPlate(self.state, self.alpha_count, self.number_count, self.variant_plate)
        
        
        return (plate_number)
    
    