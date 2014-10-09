#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont
import random
from image_to_binary import *

resolution = (1024, 768)

background_color = (255)
foreground_color = (0)


mainFont = ImageFont.truetype("./fonts/LiberationMono-Regular.ttf", 500)
subFont = ImageFont.truetype("./fonts/LiberationMono-Regular.ttf", 45)


mainText = "{:0>2d}m".format(random.randint(0, 25)).rjust(3)
subText="Get the app, http://fake.url/"

im = Image.new('L', resolution, background_color)

draw  =  ImageDraw.Draw(im)
draw.text((25, 65), mainText, font=mainFont, fill=foreground_color)
draw.text((50, 600), subText, font=subFont, fill=foreground_color)
del draw

im = im.transpose(Image.ROTATE_270)


im.show()
# image_to_bytes_to_file(im, "/dev/fb0")

