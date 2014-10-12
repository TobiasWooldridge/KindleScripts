import subprocess
import random
from image_to_binary import *

class Kindle:
    @staticmethod
    def _command(command):
        proc = subprocess.Popen(command, stdout=subprocess.PIPE)
        return proc.stdout.read()

    @staticmethod
    def display_image(im):
        if Kindle.on_kindle():
            im = im.transpose(Image.ROTATE_270)
            image_to_bytes_to_file(im, "/dev/fb0")
            Kindle.refresh_screen()
        else:
            im.show()

    @staticmethod
    def refresh_screen():
        Kindle._command(["../refresh-display"])

    @staticmethod
    def on_kindle():
        return 'kindle' in Kindle._command(['uname', '-a'])

    @staticmethod
    def battery_capacity():
        if Kindle.on_kindle():
            return int(Kindle._command(["cat", "/sys/devices/system/yoshi_battery/yoshi_battery0/battery_capacity"])[:-2])
        else:
            return random.randint(0, 99);
