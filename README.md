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



A premium tool for luxuriously converting and modifying images for the Rexault product line.

The core feature of rexconvert is its 'hexify' option, which takes a 200x200 image file (png?) and outputs a .cpp
file containing a black and white hex representation of it, which can then be uploaded to a Bespoke Digital Pet
Development Kit Mach 1.

## macOS Installation

    cd ~
    git clone https://github.com/bandrebandrebandre/rexault-luxury-converter.git
  
If git is not installed on your computer, you should be prompted to install it.

You may need to install pip packages also...not sure which ones yet.

## Windows Installation

Install python 2.7. Download and install the "Windows x86 MSI Installer (2.7.0) (sig)" option from  https://www.python.org/download/releases/2.7/

install numpy and scipy. Not sure how to do that on windows yet.

## Basic usage

MacOS users should use the following:

    cd rexault-luxury-converter
    ./rexconvert hexify <path/to/source/image.png> <value-threshold>
   
Windows users should use the following:

    cd rexault-luxury-converter
    /Python27/python.exe code/rexconvert.py hexify <path/to/source/image.png> <value-threshold>


This will create a directory "image" in the "output" directory, which will contain three files -- hexified_image.png, 
image.cpp, and image.h. For example, invoking ./rexconvert hexify source_images/sample.png would create output/hexified_sample.png, sample.cpp, and sample.h. The idea is you can open up the png and have a look to make sure the conversion went ok before transferring the .ccp and .h files to the development unit to be rendered on the display.

The display on the Mach1 development unit can only display black or white pixels. "threshold" will convert all pixels in the image to either black or white. Playing with different values for <value-threshold> will result in different images. You can leave <value-threshold> off of the invocation entirely, and it will use a default of 127. The value should be a number between 0 and 255, where lower values will result in more black pixels, and higher will result in more white.

## Additional options

    ./rexconvert blackandwhiteify <path/to/source/image.png> <value-threshold>
    
The 'blackandwhiteify' option will simply output an image with only black and white pixels, and not create the .cpp and .h files in the hefixy option.

    ./rexconvert halftoneify <path/to/source/image.png> <sample> <scale>
    
This will create a "halftoned" version of the image. Sample and scale are both optional. Playing around with <sample> will result in different dot sizes. <sample> should be an integer. The default of <sample> is 5. The default of <scale> is 1. Increasing <scale> will simply increase the number of pixels in the image, which is generally not desirable for this, as we are dealing with a fixed 200x200 b/w display.
  
    ./rexconvert greyify <path/to/source/image.png>
    
greyify will simply output a greyscale version of the image.

    ./rexconvert shrinkify
    
shrinkify is still in development.
