#!/usr/bin/env python
from PIL import Image
import getopt
import sys

def display_help():
    print '%s -i <image path> -o [output path=/dev/fb0]' % sys.argv[0]

def image_to_bytes(im):
        return bytearray(list(im.convert("L").getdata()))

def image_to_bytes_to_file(im, file):
    im_bytes = image_to_bytes(im)

    with open(file, "w") as f:
        f.write(im_bytes)


if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:],"i:o:h:w:",["help","input=","output=","width=","height="])
    except getopt.GetoptError:
        display_help()
        sys.exit(2)

    inputfile = None
    outputfile = "/dev/fb0"
    width = -1
    height = -1

    for opt, arg in opts:
        if opt == '--help':
            display_help()
            sys.exit(0)
        elif opt in ('-i', '--input'):
            inputfile = arg
        elif opt in ('-o', '--output'):
            outputfile = arg
        elif opt in ('-w', '--width'):
            width = int(arg)
        elif opt in ('-h', '--height'):
            height = int(arg)

    # Verify essential arguments
    if None in (inputfile, outputfile):
        display_help()
        sys.exit(2)

    # Load image
    im = None
    try:
        im = Image.open(inputfile, "r")
    except IOError:
        print "Could not open input image from file '%s'" % inputfile
        sys.exit(2)

    # Resize image if requested
    if -1 not in (width, height):
        im = im.resize((width, height))

    # Convert the image to black and white
    image_to_bytes_to_file(im, outputfile)
