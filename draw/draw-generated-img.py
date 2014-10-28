#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont
import platform
import time
from kindle import Kindle
from pytz import timezone
import datetime
import json
import urllib2
import math


class BaseFrame:
    _resolution = (1024, 768)

    _bg_color = (255)
    _fg_color = (0)
    _pale_color = (128)

    def __init__(self):
        self._monoRegular = "./fonts/LiberationMono-Regular.ttf"
        self._sansRegular = "./fonts/LiberationSans-Regular.ttf"

        self._batteryFont = ImageFont.truetype(self._sansRegular, 20)

    def draw_frame(self, draw, state):
        """ This is a no-op"""

    def _draw_battery_warning(self, draw, capacity):
        if capacity > 50:
            return

        color = self._pale_color

        if capacity < 5:
            color = self._fg_color
            warning = "This screen may be frozen."
        elif capacity < 15:
            warning = "This screen may freeze soon."
        else:
            warning = "Power may have been disconnected."


        draw.text((50, 730), "Warning: Battery capacity is {0}%. {1}".format(capacity, warning), font=self._batteryFont, fill=self._pale_color)

    def draw(self, state):
        im = Image.new('LA', self._resolution, self._bg_color)
        draw = ImageDraw.Draw(im)

        self._draw_battery_warning(draw, Kindle.battery_capacity())
        self.draw_frame(draw, state)

        return im

class BusTimeFrame(BaseFrame):
    def __init__(self):
        BaseFrame.__init__(self)

        self._mainFont = ImageFont.truetype(self._monoRegular, 600)
        self._mainTailFont = ImageFont.truetype(self._sansRegular, 150)
        self._smallFont = ImageFont.truetype(self._sansRegular, 45)
        self._tinyFont = ImageFont.truetype(self._sansRegular, 25)

    def draw_frame(self, draw, state):
        mainText = "{: >2d} ".format(state['mins']).rjust(3)
        mainTailText = "min"
        subText="Until the next Loop Bus arrives"
        subTextTwo="Get the app or track the bus online: http://loopb.us/"

        # Because we're using LiberationMono, 0 has a dot in the middle but O doesn't, meaning O looks nicer
        mainText = mainText.replace('0', 'O')

        draw.text((10, 0), mainText, font=self._mainFont, fill=self._fg_color)
        draw.text((750, 365), mainTailText, font=self._mainTailFont, fill=self._fg_color)
        draw.text((0, 15), "___", font=self._mainFont, fill=self._fg_color)
        draw.text((50, 630), subText, font=self._smallFont, fill=self._fg_color)
        draw.text((50, 690), subTextTwo, font=self._tinyFont, fill=self._fg_color)

fb = BusTimeFrame()

# capacity = Kindle.battery_capacity()
# im = fb.generate_waiting_image(capacity)
# Kindle.display_image(im)

def getMins():
    print "Loading predictions"
    predictions = json.load(urllib2.urlopen('http://tracker.tobias.tw/predictions.php'))


    silcPrediction = None
    for prediction in predictions:
        if prediction['id'] == 5:
            silcPrediction = prediction
            break

    return int(math.floor(silcPrediction['prediction'] / 60.0))

    # adelaide = timezone("Australia/Adelaide")
    # dt = datetime.datetime.now(adelaide)
    

mins = -1
while True:
    latestMins = getMins()
    if mins != latestMins:
        mins = latestMins
        im = fb.draw({ 'mins' : mins})
        Kindle.display_image(im)

    time.sleep(1)

