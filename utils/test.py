import cv2
import os
import string

s_img = cv2.imread("/home/nexlson/Desktop/Malaysia_Licence_Plate_Generator/data/Arial_Bold/reversed/alphabets/A.png")
l_img = cv2.imread("/home/nexlson/Desktop/Malaysia_Licence_Plate_Generator/data/backplate/double_line_backplate.jpg")
alphabetsString = string.ascii_uppercase
y_offset=25
x_offset = 50
remaining_space_x = back_plate.shape[1] - (x_offset*2)
per_space = int(remaining_space_x / len(plate_number))
remaining_space_y =  back_plate.shape[0] - (y_offset*2)
half = remaining_space_y / 2
for alphabet in plate_number:
    if alphabet in alphabetsString:
        charPath = self.getCharPath(alphabet, "Arial_Bold")
        img = self.readImage(charPath)
        back_plate[y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1]] = img
        x_offset += per_space
    else:
        y_offset += half
        charPath = self.getCharPath(alphabet, "Arial_Bold")
        img = self.readImage(charPath)
        back_plate[y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1]] = img
        x_offset += per_space


cv2.imshow("Test",l_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

alphabetsString = string.ascii_uppercase
print(alphabetsString)
if '1' in alphabetsString:
    print('yey')