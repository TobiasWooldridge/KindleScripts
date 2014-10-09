Kindle Draw
===========

Paint an image to your Kindle PaperWhite display by using the framebuffer

This tool simply takes an image, converts it to binary (1 pixel = 1 byte) and dumps it to your Kindle's framebuffer (/dev/fb0) before forcing a screen refresh

It depends on python and python-imaging (I'm running these from Debian as a chroot on my kindle)

```apt-get install python python-imaging```

Usage
-----

```
# Explode the image into its bytes
python image-to-binary.py -i input.png -o output.bin -w 768 -h 1024

# Dump the bytes to the frame buffer
dd if=output.bin of=/dev/fb0 bs=768 count=1024

# Force a screen refresh
echo 1 > /sys/devices/platform/mxc_epdc_fb/mxc_epdc_update
```

Notes
-----

* The bytes you dump to /dev/fb0 start at the top of the screen, and scan lines start from the left.

* Make sure your image width aligns to the display screen width (for a PaperWhite, this is 768px) or your image will look incredibly distored

* The PaperWhite's display size is 768x1024

* The '(eips)[http://wiki.mobileread.com/wiki/Eips]' command (exists by default on kindle) seems to use some form of pixel scaling or similar that I didn't care to investigate, hence I wrote this. It is still useful for clearing the screen/etc.

* Because some parts of your kindle's display update automatically (e.g. the time), it's probably best to use this while the screensaver is enabled (as that ensures the Kindle firmware won't try to update the display)
