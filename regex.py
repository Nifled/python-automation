import re

haha = 'HaHaHa'

m = re.findall(r'(Ha)', haha)

print(m[2])
