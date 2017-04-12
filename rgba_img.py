# Using Pillow
from PIL import Image, ImageColor

# First arg for _getcolor() is string represented color (case insensitive) and second is 'RGBA', returns tuple.
# Pillow supports a huge number of color names, from 'aliceblue' to'whitesmoke'.
red = ImageColor.getcolor('red', 'RGBA')
black = ImageColor.getcolor('Black', 'RGBA')
choc = ImageColor.getcolor('chocolate', 'RGBA')

# --------------------------------------------------
# Manipulating Images with Pillow

# For selecting a region in an image, with Pillow, it expects a tuple of 4 ints.
# Left: The x-coordinate of the leftmost edge of the box
# Top: The y-coordinate of the top edge of the box.
# Right: The x-coordinate of one pixel to the right of the rightmost edge of the box. This integer must be greater than the left integer
# Bottom: The y-coordinate of one pixel lower than the bottom edge of the box. This integer must be greater than the top integer.

# image of cat
cat = Image.open('image.png')

img_size = cat.size  # or 'width, height = cat.size'
img_format = cat.format

# Saves NEW image to disc with the given name and format.
cat.save('cat.png')

# Create new Image object (without saving to disc).
# Arguements = 'RGBA' to set color, (100,200) for size, and 'purple' for color string.
img1 = Image.new('RGBA', (100, 200), 'purple')
img1.save('purpleImg.png')

img2 = Image.new('RGBA', (20, 20))  # Transparent img
# Invisible black, (0, 0, 0, 0), is the default color used if no color argument is specified
img2.save('transparent.png')

# --------------------------------------------------
# Cropping Images

# Doesn't affect image directly, creates new Image object
# Takes in boxed tuple as arg (the Left, Top, Right, Bottom explained on up there ^).
croppedIm = cat.crop((335, 345, 565, 560))  # Set values accordingly to image size.
croppedIm.save('cropped.png')

# --------------------------------------------------
# Resizing Images

width, height = cat.size
quarter_sized_cat = cat.resize((int(width / 2), int(height / 2)))
quarter_sized_cat.save('quartersized.png')  # Doesn't crop, it RESIZES.

# --------------------------------------------------
# Changing Individual Pixels of an Image

img = Image.new('RGBA', (100, 100))  # Transparent image
img.getpixel((0, 0))  # Gets tuple representing x,y of pixel (returns '(0, 0, 0, 0)').
img.save('pixels.png')

for x in range(100):
    for y in range(50):
        img.putpixel((x, y), (210, 210, 210))  # Fills half of image pixels with light grey.

for x in range(100):
    for y in range(50, 100):  # 50, 51, 52, 53, ...
        img.putpixel((x, y), ImageColor.getcolor('green', 'RGBA'))

img.save('colored_pixels.png')
