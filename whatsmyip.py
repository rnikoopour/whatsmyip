#!/usr/bin/env python3

import bs4
import re
import requests

response = requests.get('http://www.ipchicken.com')
soup = bs4.BeautifulSoup(response.text, 'html.parser')
ip = re.findall('\d+\.\d+\.\d+\.\d+', soup.b.text)[0]
print(ip)

