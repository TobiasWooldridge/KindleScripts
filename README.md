KindleScripts
=============

This repo includes a bunch of scripts for doing various things on a Kindle PW

Primitives
----------

General commands are located in the root directory. Usage includes

```
./block-ota-updates # blocks over-the-air Kindle updates
./prevent-ss # Prevents screensaver from starting. Need to restart kindle to re-enable SS
./refresh-display # Forces a refresh of the Kindle's eink display
./set-brightness 254 # Set the brightness of the Kindle's frontlight to a value between 0 and 254 (inclusive)
```

Debian
------

Used for installing/running debian as a chroot on a Kindle (my build env of choice)

```
./debian/create-debian-image # Run on Debian/Ubuntu to bootstrap debian.ext3 (A sys partition containing Debian built for armel). Copy this to your Kindle via USB (or scp it to /mnt/base-us/debian.ext3)
./debian/mount-debian # Mounts /mnt/base-us/debian.ext3 as /mnt/debian
./debian/setup-debian # Completes the debootstrap second stage process, adds apt-get repos and installs software in Debian (e.g. python + git). Requires mount-debian to be called first
./debian/umount-debian # Unmounts /mnt/debian
./debian/chroot-debian # Chroot into debian
```


Draw
----

Used for drawing images to the Kindle's display. See [draw/README.md](draw/README.md)

```
./draw/draw-image draw/test.png # Draws the image draw/test.png to the Kindle's eink display by writing it to the framebuffer
./draw/image-to-binary.py -h # Converts any image file to a raw bitmap file to dump to the Kindle PaperWhite's frame buffer (/dev/fb0)
./draw/draw-noise # Draws noise to the Kindle's eink display
```



