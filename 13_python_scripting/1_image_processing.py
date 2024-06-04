# image processing

# Pillow - is a program that we will use
# pip3 install pillow

from PIL import Image, ImageFilter

img = Image.open('./images/pikachu.jpg')

# <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x640 at 0x102916390>
print(img)

print(img.format)  # JPEG
print(img.size)  # (640, 640)
print(img.mode)  # RGB

filtered_img = img.filter(ImageFilter.BLUR)

# changing to png from jpg because it supports the image filters.
filtered_img.save("blur.png", 'png')


filtered_img = img.filter(ImageFilter.SMOOTH)

filtered_img.save("smooth.png", 'png')

# black and white... uses "L"
filtered_img = img.convert('L')
filtered_img.save("grey.png", 'png')

# filtered_img.show() # will open the image in another program

crooked = filtered_img.rotate(90)

crooked.save('crooked.png', 'png')

resize = filtered_img.resize((300, 300))  # is a tuple so has to be in inner ()
resize.save('resize.png', 'png')

box = (100, 100, 400, 400)
region = filtered_img.crop(box)

region.save('cropped.png', 'png')
