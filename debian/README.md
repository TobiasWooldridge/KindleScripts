Kindle scripts Debian
=====================

The files in this directory are used for creating and managing a debian image on
the Amazon Kindle PaperWhite (though they probably work for other versions)


Part 1: Creating a Debian ext3 disk image
-----------------------------------------

These scripts rely on the existence of an ext3 file partition image containing
Debian.

An ext3 fs image containing Debian can be made using the
```create-debian-image``` tool.

This needs to be run on an Ubuntu or Debian machine. It depends on the
'debootstrap' utility and makes a Debian image for the Armel architecture.

Part 2: Copying the image to the Kindle
---------------------------------------

The debian image then needs to be copied to the Kindle device over its USB-net
connection.

This can be achieved using

```scp debian.ext3 root@192.168.15.244:/mnt/base-us```

which will copy the image to the base-us directory on the Kindle.

The scripts in this directory need to then be copied to the kindle. From the
parent of the KindleScripts directory, run

```scp -r KindleScripts root@192.168.15.244:/mnt/base-us/scripts```


Part 3: Completing the Debian installation
------------------------------------------

Then SSH to the Kindle and run the following commands

```
cd /mnt/base-us/scripts
bash debian/setup-debian
```


```debian/setup-debian``` is responsible for the second stage of the Deboostrap
process, and setting up Debian in other ways (e.g. sets nameservers, apt-get
repos, etc.)



Part 4: Chrooting to Debian
------------------------------------------

This lets you run programs under debian. This means you can now install stuff
like python in debian, to run python apps in debian, or you can compile programs
in debian for the Armel architecure without needing to worry about the overhead
of cross compiling for the platform.

Just mount debian if it isn't already mounted, using

```bash debian/mount-debian```

And then use

```bash debian/chroot-debian```

to chroot into it. 

From a usage perspective this is similar to using a virtual machine, except
you're just using a virtual root filesystem.
