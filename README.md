# reXconvert -- The Luxury Image Conversion Tool
<pre>
                     /$$   /$$                                                               /$$    
                    | $$  / $$                                                              | $$    
  /$$$$$$   /$$$$$$ |  $$/ $$/  /$$$$$$$  /$$$$$$  /$$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$  /$$$$$$  
 /$$__  $$ /$$__  $$ \  $$$$/  /$$_____/ /$$__  $$| $$__  $$|  $$  /$$//$$__  $$ /$$__  $$|_  $$_/  
| $$  \__/| $$$$$$$$  >$$  $$ | $$      | $$  \ $$| $$  \ $$ \  $$/$$/| $$$$$$$$| $$  \__/  | $$    
| $$      | $$_____/ /$$/\  $$| $$      | $$  | $$| $$  | $$  \  $$$/ | $$_____/| $$        | $$ /$$
| $$      |  $$$$$$$| $$  \ $$|  $$$$$$$|  $$$$$$/| $$  | $$   \  $/  |  $$$$$$$| $$        |  $$$$/
|__/       \_______/|__/  |__/ \_______/ \______/ |__/  |__/    \_/    \_______/|__/         \___/  
</pre>



A premium tool for luxuriously converting and modifying images for the Rexault luxury product line.

The core feature of rexconvert is its 'hexify' option, which takes a 200x200 image file (png?) and outputs a .cpp
file containing a black and white hex representation of it which, which can then be uploaded to a Bespoke Digital Pet
Development Kit Mach 1.

## Installation

(Assumes macOS)

    cd ~
    git clone https://github.com/bandrebandrebandre/rexault-luxury-converter.git
  
If git is not installed on your computer, you should be prompted to install it.

You may need to install pip packages also...not sure which ones yet.

## Basic usage

    cd rexault-luxury-converter
    ./rexconvert hexify <path/to/source/image.png> 
   
   
This will create a directory "image" in the "output" directory, which will contain three files -- hexified_image.png, 
image.cpp, and image.h. For example, invoking ./rexconvert hexify source_images/sample.png would create output/hexified_sample.png, sample.cpp, and sample.h. The idea is you can open up the png and have a look to make sure the conversion went ok before transferring the .ccp and .h files to the development unit to be rendered on the display.

## Additional options

shrinkify
blackandwhiteify
halftoneify
greyify
