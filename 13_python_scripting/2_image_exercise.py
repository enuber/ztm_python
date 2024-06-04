# JPG to PNG converter
# will take first the name of the folder that exists with images in it. "images/"
# second will take the name of the folder to put the images into "new/"

from PIL import Image, ImageFilter
import sys
import os

# grab first and second arguments (ie name of folders)
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if second argument folder name exists or not, if not then create it.
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through existing photos
# convert images to png
# save to the new folder

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    # this gives us back ('filename', 'extension') since it's a tuple we just want the filename
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
print('all done!')
