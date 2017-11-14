from PIL import Image
import pytesseract
import cv2
import numpy as np
import sys
import os.path


if len(sys.argv[1]) == 0:
    print ("please enter input file")
    sys.exit()
else:
    input_file = sys.argv[1]

im = Image.open(input_file)

text = pytesseract.image_to_string(im, lang = 'eng')

print(text)
