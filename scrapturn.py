import requests as rqs
from bs4 import BeautifulSoup as bsp

data = rqs.get('https://g1.globo.com/')
soup = bsp(data.text, 'html.parser')

import numpy as np
import tensorflow as tf
headers = [span.text for span in soup.find_all('div', {'class': 'feed-post-header with-post-chapeu'})]
title = [span.text for span in soup.find_all('div', {'class': 'feed-post-body-title gui-color-primary gui-color-hover'})]
review = [span.text for span in soup.find_all('div', {'class': 'feed-post-body-resumo'})]

print("Headers")
print(headers)
print("Title")
print(title)
print("Review")
print(review)
