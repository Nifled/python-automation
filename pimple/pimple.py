import os
from PIL import Image

# \
#  Pre-defined constants
# /
IMAGE_QUALITY = 75
RESIZE_OPTION = True
RESIZE_PERCENT = 50
RES_THRESHOLD = (1080, 720)

# TEMP
DIRNAME = '.'

def checks(w, h):
    """w = Width, h = Height"""
    if w < RES_THRESHOLD[0] and h < RES_THRESHOLD[1]:
        return True
    return False

def resize_img(_img):
    w, h = _img.size
    new_w, new_h = w * RESIZE_PERCENT / 100, h * RESIZE_PERCENT / 100

    _img.thumbnail((new_w, new_h), Image.ANTIALIAS)
    return


def compress_img(file_name, resize=False):
    print(file_name)
    ext = file_name.rsplit('.')[-1]
    if not (ext == 'png' or ext == 'jpg'):
        return

    image = Image.open(file_name)

    if resize:
        resize_img(image)

    image.save(
        os.path.join('popped', file_name),
        optimize=True,
        quality=IMAGE_QUALITY
    )

def compress_dir(dirname):
    for file_name in os.listdir(dirname):
        compress_img(file_name, resize=RESIZE_OPTION)
    return


def main():
    os.makedirs('popped', exist_ok=True)

    print('Optimizing images...')

    compress_dir(DIRNAME)

    print('Done!')

if __name__ == '__main__':
    main()
