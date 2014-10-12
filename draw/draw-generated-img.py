#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont
import platform
import time
from kindle import Kindle

class FrameGenerator:
    resolution = (1024, 768)

    background_color = (255)
    foreground_color = (0)

    mainFont = ImageFont.truetype("./fonts/LiberationMono-Regular.ttf", 600)
    mainTailFont = ImageFont.truetype("./fonts/LiberationSans-Regular.ttf", 150)
    smallFont = ImageFont.truetype("./fonts/LiberationSans-Regular.ttf", 45)
    tinyFont = ImageFont.truetype("./fonts/LiberationMono-Regular.ttf", 25)

    def generate_waiting_image(self, time):
        mainText = "{: >2d} ".format(time).rjust(3)
        mainTailText = "min"
        subText="Until the next Loop Bus arrives"
        subTextTwo="Get the app, http://fake.url/"

        # Because we're using LiberationMono, 0 has a dot in the middle but O doesn't
        mainText = mainText.replace('0', 'O')


        im = Image.new('L', self.resolution, self.background_color)

        draw  =  ImageDraw.Draw(im)
        draw.text((10, 0), mainText, font=self.mainFont, fill=self.foreground_color)
        draw.text((750, 365), mainTailText, font=self.mainTailFont, fill=self.foreground_color)
        draw.text((0, 15), "___", font=self.mainFont, fill=self.foreground_color)
        draw.text((50, 630), subText, font=self.smallFont, fill=self.foreground_color)
        draw.text((50, 690), subTextTwo, font=self.tinyFont, fill=self.foreground_color)
        del draw

        return im

fb = FrameGenerator()


capacity = Kindle.battery_capacity()
im = fb.generate_waiting_image(capacity)
Kindle.display_image(im)

# capacity = 0
# while True:
#     if capacity != Kindle.battery_capacity():
#         capacity = Kindle.battery_capacity()
#         im = fb.generate_waiting_image(capacity)
#         Kindle.display_image(im)
#     time.sleep(10)

