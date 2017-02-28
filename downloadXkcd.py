#! python3
# downloadXkcd.py - Downloads every single XKCD comic off https://xkcd.com/ navigating through 'previous posts'.

import requests
import os
import bs4

url = 'https://xkcd.com'  # Starting URL
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd dir

# The first comic’s Prev button links to the http://xkcd.com/# URL, indicating
# that there are no more previous pages. So...
while not url.endswith('#'):

    # Download the current page.
    print('Downloading page {}...'.format(url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    comic_img = soup.select('#comic > img')

    if not comic_img:
        print('Couldn\'t find comic image.')
    else:
        img_url = 'http:' + comic_img[0].get('src')  # Get comic's image URL.

        # Download comic image
        print('Downloading image {}...'.format(img_url))
        res = requests.get(img_url)
        res.raise_for_status()

        # Save the image to ./xkcd
        with open(os.path.join('xkcd', os.path.basename(img_url)), 'wb') as img_file:

            for chunk in res.iter_content(100000):
                img_file.write(chunk)
            img_file.close()

    # Get the Previous button's URL.
    prev_link = soup.select('a[rel="prev"]')[0]  # Previous link
    # prev_link = soup.select('.comicNav li')[1]  --- Other way to get previous button link.

    url = 'http://xkcd.com' + prev_link.get('href')  # Override url var with previous button's URL.

print('Done.')
