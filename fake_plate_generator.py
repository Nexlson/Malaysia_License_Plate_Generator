import cv2 
import os
import random
import logging
import string

class Generator():
    def getCharPath(self, alphabet, font, plate_type):
        if plate_type == "putrajaya":
            path = str(os.getcwd()) + '/data/Calisto/reversed/{}.png'.format(alphabet)
            return path
        path = str(os.getcwd()) + '/data/{}/reversed/characters/{}.png'.format(font, alphabet)
        return path
    
    def getRandomPlate(self, stateName, front_alpha_num, num_num, variant, plate_type):
        # Constant
        state = {"Perak": "A", "Selangor": "B", "Pahang": "C", "Kelantan": "D", "Putrajaya": "F", 
        "Johor": "J", "Kedah": "K", "Malacca": "M", "Negeri Sembilan": "N", "Penang": "P",
        "Perlis": "R", "Kuala Lumpur(1)": "W", "Kuala Lumpur(2)": "V", "Sarawak": "Q", "Sabah": "S"}
        alphabets_number = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q",
        "R", "S", "T", "U", "V", "W", "X", "Y"]
        special = 'Putrajaya'
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
        # Putrajaya plate 
        if plate_type == "putrajaya":
            plate = special + ' ' + number_group
            return plate
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

    def generatePlates(self, plate_type, total_plate, variant_plate ,state, alphabet_num, number_num, font_type, display):
        # Import plate type
        plate_path = str(os.getcwd()) + '/data/backplate/'
        if plate_type == "double":
            name = 'double_line_backplate.jpg'
            back_plate = self.readImage(plate_path+name)
        else:
            name = 'single_line_backplate.jpg'
            back_plate = self.readImage(plate_path+name)
        
        # Loop for several times 
        for count in range(total_plate):
            # Generate random car plate
            plate_number = self.getRandomPlate(state, alphabet_num, number_num, variant_plate, plate_type)
            print("Generating fake car plate for {}".format(plate_number))
            # Import characters based on plate number

            # Merge backplate and characters
            print("Merging backplate and characters...")
            # Constant
            # X and y starting 
            y_offset=25
            x_offset = 50
            # Remaining space for characters
            remaining_space = back_plate.shape[1] - (x_offset*2)
            alphabetsString = string.ascii_uppercase
            # Space remaining for font
            per_space = int(remaining_space / len(plate_number))
            # Y starting point for second row
            remaining_space_y =  back_plate.shape[0] - (y_offset*2)
            secondHalf = y_offset + int(remaining_space_y / 2)
            
            if plate_type == "single":
                for alphabet in plate_number:
                    charPath = self.getCharPath(alphabet, font_type, plate_type)
                    img = self.readImage(charPath)
                    back_plate[y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1]] = img
                    x_offset += per_space

            elif plate_type == "putrajaya":
                listPlate = plate_number.split(" ")
                putraChar = listPlate[0]
                remainChar = listPlate[1]
                putraCharPath = self.getCharPath("Putrajaya", font_type, plate_type)
                putraImg = self.readImage(putraCharPath)
                back_plate[y_offset:y_offset+putraImg.shape[0], x_offset:x_offset+putraImg.shape[1]] = putraImg
                x_offset += putraImg.shape[1]
                plate_type = "single"
                for alphabet in remainChar:
                    charPath = self.getCharPath(alphabet, font_type, plate_type)
                    print(charPath)
                    img = self.readImage(charPath)
                    back_plate[y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1]] = img
                    x_offset += img.shape[1] + 25

            elif plate_type == "double":
                front_alpha = ''
                back_num = ''
                first_x_offset = second_x_offset = x_offset
                first_x_offset = 100
                second_x_offset = 50
                for alphabet in plate_number:
                    if alphabet in alphabetsString:
                        front_alpha += alphabet
                    else:
                        back_num += alphabet
                first_remaining_space = back_plate.shape[1] - (first_x_offset*2)
                second_remaining_space = back_plate.shape[1] - (second_x_offset*2)
                first_per_space = int(first_remaining_space / len(front_alpha))
                second_per_space = int(second_remaining_space / len(back_num))
                for alphabet in front_alpha:
                    charPath = self.getCharPath(alphabet, font_type, plate_type)
                    img = self.readImage(charPath)
                    back_plate[y_offset:y_offset+img.shape[0], first_x_offset:first_x_offset+img.shape[1]] = img
                    first_x_offset += first_per_space
                for alphabet in back_num:
                    y_offset = secondHalf
                    charPath = self.getCharPath(alphabet, font_type, plate_type)
                    img = self.readImage(charPath)
                    back_plate[y_offset:y_offset+img.shape[0], second_x_offset:second_x_offset+img.shape[1]] = img
                    second_x_offset += second_per_space

            # Show if want
            if display:
                print("Showing output")
                cv2.imshow("Generated plate", back_plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            
            # Save output
            print("Fake car plate, {} is saved".format(plate_number))
            dest_path = str(os.getcwd()) + '/data/generated_plates/{}.jpg'.format(plate_number)
            cv2.imwrite(dest_path, back_plate)
        return
         
    