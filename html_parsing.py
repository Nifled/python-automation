import bs4
import requests

res = requests.get('https://www.nostarch.com/automatestuff/')

# Checks if response went through successfully. If not, program stops.
res.raise_for_status()

# The 'html.parser' is just to say what parser var soup will use.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# var soup will be a BeautifulSoup Object

# Example of the bs4 select() method.
elems = soup.select('div > span')
# elems will be a 'list' object (list of tags). Can be used, iterated, etc like a normal list.

# Gets the text that's inside the tags
tag_text = elems[0].getText()

# attrs returns a dict with the attributes that the tag has, like the CSS class, id, style, etc.
attributes = elems[1].attrs

# get() method for Tag objects to access attribute values from an element. Example below.
elem_id = elems[1].get('class')

print(elem_id)
