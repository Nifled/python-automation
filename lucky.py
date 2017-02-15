#! python3
# lucky.py - Opens several Google search results.

# Instructions to run script directly in Windows/Linux on Appendix B from book.

import requests
import sys
import webbrowser
import bs4

print('Googling...')  # Display text while downloading the Google page

# Gets query from command line
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()  #Script stops if request fails.

# Get search result links page
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Gets the specific link elements (now BeatifulSoup objects)
top_links = soup.select('.r a')

# Gets top 3 results, if links are fewer than 5, it gets all.
numOpen = min(3, len(top_links))

for i in range(numOpen):
    webbrowser.open_new_tab('http://google.com' + top_links[i].get('href'))
