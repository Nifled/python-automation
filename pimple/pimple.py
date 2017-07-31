import os
from PIL import Image

os.makedirs('popped', exist_ok=True)

print('Optimizing images...')

for file_name in os.listdir('.'):
    if not (file_name.endswith('.png') or file_name.endswith('.jpg')):
        continue

    img = Image.open(file_name)
    img.save(os.path.join('popped', file_name), optimize=True)
