#!/usr/bin/env python2.7

from scipy import misc as MSC
import os, sys
from PIL import Image
import math
from halftone import halftone

threshold = 125

def hexify(path, width, height, image_name):
    code = \
    '''\rconst unsigned char %s[] PROGMEM = {\r/* Generated by


                     /$$   /$$                     /$$   /$$                              
                    | $$  / $$                    | $$  | $$                              
  /$$$$$$   /$$$$$$ |  $$/ $$/  /$$$$$$  /$$   /$$| $$ /$$$$$$                            
 /$$__  $$ /$$__  $$ \  $$$$/  |____  $$| $$  | $$| $$|_  $$_/                            
| $$  \__/| $$$$$$$$  >$$  $$   /$$$$$$$| $$  | $$| $$  | $$                              
| $$      | $$_____/ /$$/\  $$ /$$__  $$| $$  | $$| $$  | $$ /$$                          
| $$      |  $$$$$$$| $$  \ $$|  $$$$$$$|  $$$$$$/| $$  |  $$$$/                          
|__/       \_______/|__/  |__/ \_______/ \______/ |__/   \___/                            
                                                                                          
                                                                                          
                                                                                          
 /$$           /$$   /$$                                                                  
| $$          | $$  / $$                                                                  
| $$ /$$   /$$|  $$/ $$/ /$$   /$$  /$$$$$$  /$$   /$$                                    
| $$| $$  | $$ \  $$$$/ | $$  | $$ /$$__  $$| $$  | $$                                    
| $$| $$  | $$  >$$  $$ | $$  | $$| $$  \__/| $$  | $$                                    
| $$| $$  | $$ /$$/\  $$| $$  | $$| $$      | $$  | $$                                    
| $$|  $$$$$$/| $$  \ $$|  $$$$$$/| $$      |  $$$$$$$                                    
|__/ \______/ |__/  |__/ \______/ |__/       \____  $$                                    
                                             /$$  | $$                                    
                                            |  $$$$$$/                                    
                                             \______/                                     
  /$$$$$$                                                      /$$      /$$$$$$           
 /$$__  $$                                                    | $$     /$$$_  $$          
| $$  \__/  /$$$$$$  /$$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$  /$$$$$$  | $$$$\ $$  /$$$$$$ 
| $$       /$$__  $$| $$__  $$|  $$  /$$//$$__  $$ /$$__  $$|_  $$_/  | $$ $$ $$ /$$__  $$
| $$      | $$  \ $$| $$  \ $$ \  $$/$$/| $$$$$$$$| $$  \__/  | $$    | $$\ $$$$| $$  \__/
| $$    $$| $$  | $$| $$  | $$  \  $$$/ | $$_____/| $$        | $$ /$$| $$ \ $$$| $$      
|  $$$$$$/|  $$$$$$/| $$  | $$   \  $/  |  $$$$$$$| $$        |  $$$$/|  $$$$$$/| $$      
 \______/  \______/ |__/  |__/    \_/    \_______/|__/         \___/   \______/ |__/                                                                


 -- a luxury, ultrapremium image conversion script. */  
''' % image_name

    #if width is 11, row size is 2. if width is 20, row_size is 3. 
    image = MSC.imread(path)
    bin_array = [[] for i in range(height)]

    for y in range(0, height):
        bin_array[y] = ""
        for x in range(0, width):
            if image[y][x][0] < threshold:
                image[y][x][0] = 0
                bin_array[y] += "0"
            else: 
                image[y][x][0] = 255
                bin_array[y] += "1"

    row_size_in_bytes = int(math.ceil(width / 8))
    byte_counter = 0

    for y in range(0, len(bin_array)):
        for byte in range(0, row_size_in_bytes):
            hexified = hex(int(bin_array[y][(byte * 8):min(((byte+1) * 8), width)], 2)).upper()
            code += hexified
            if len(hexified) == 3:
                code += "0"
            code += ","
            byte_counter += 1
            if byte_counter == 15:
                code += "\r"
                byte_counter = 0
    if code[:1] != '\r':
        code += '\r'      
    code += '};'
    with open('hexy' + image_name + ".cpp", 'w') as hexy_out:
        hexy_out.write(code)

    Image.fromarray(image).save("bw" + image_name + ".png")


def greyify(path, width, height, image_name):
    im = Image.open(path, 'r')
    greyim = im.convert("LA") # greyscale
    greyim.save("grey"+image_name, "PNG")
    hexify("grey" +image_name, width, height, image_name)


def halftoneify(path, width, height, image_name):
    h = halftone.Halftone(path)
    h.make(filename_addition='_halftoneified', style='grayscale', sample=1, scale=10)


def shrinkify(path, width, height, image_name):
    size = width, height
    im = Image.open(path)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(image_name, "PNG")
#    greyify(image_name, width, height, image_name)
    halftoneify(image_name, width, height, image_name)


if __name__ == "__main__":
    shrinkify(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
