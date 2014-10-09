#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont
import random
from image_to_binary import *

resolution = (1024, 768)

background_color = (255)
foreground_color = (0)


mainFont = ImageFont.truetype("./fonts/LiberationMono-Regular.ttf", 555)
subFont = ImageFont.truetype("./fonts/LiberationMono-Regular.ttf", 45)
subFontTwo = ImageFont.truetype("./fonts/LiberationMono-Regular.ttf", 25)


mainText = "{: >2d}m".format(random.randint(0, 25)).rjust(3)
subText="Until the next Loop Bus arrives"
subTextTwo="Get the app, http://fake.url/"

im = Image.new('L', resolution, background_color)

draw  =  ImageDraw.Draw(im)
draw.text((10, 35), mainText, font=mainFont, fill=foreground_color)
draw.text((10, 65), "___", font=mainFont, fill=foreground_color)
draw.text((50, 630), subText, font=subFont, fill=foreground_color)
draw.text((50, 690), subTextTwo, font=subFontTwo, fill=foreground_color)
del draw


im = im.transpose(Image.ROTATE_270)
image_to_bytes_to_file(im, "/dev/fb0")


# im.show()

