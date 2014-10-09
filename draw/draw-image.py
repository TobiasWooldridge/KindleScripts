from PIL import Image

im = Image.open("input.png", "r")

# Convert the image to black and white
img_data = list(im.convert("L").getdata())


# img_data = list()

# (width, height) = im.size

# for x in range(0, width):
#     for y in range(0, height):
#         img_data.append(im.getpixel((x, y)))


img_bytes = bytearray(img_data)


with open("output.bin", "w") as f:
    f.write(img_bytes)
