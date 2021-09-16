import requests as rqs
from bs4 import BeautifulSoup as bsp
import json
from datetime import datetime

data = rqs.get('https://g1.globo.com/')
scraptime = datetime.now()
soup = bsp(data.text, 'html.parser')

scrapped_data = {
        'full_content': [span.text for span in soup.find_all('div', {'class':'feed-post-body'})],
        'headers':[span.text for span in soup.find_all('div', {'class': 'feed-post-header with-post-chapeu'})],
        'title':[span.text for span in soup.find_all('div', {'class': 'feed-post-body-title '
                                                                         'gui-color-primary gui-color-hover'})],
        'review':[span.text for span in soup.find_all('div', {'class': 'feed-post-body-resumo'})],
        'related':[span.text for span in soup.find_all('div', {'class': 'bstn-fd-relatedtext'})],
        'feed_time':[span.text for span in soup.find_all('div', {'class': 'feed-post-metadata'})],
        'scraptime': scraptime.strftime('%d/%m/%Y %H:%M')
    }

print(json.dumps(scrapped_data, indent=4, ensure_ascii=False))
aux = scraptime.strftime('%d-%m-%Y %H-%M')
with open(f"json/outputg1({aux}).json", 'w') as outfile:
    json.dump(scrapped_data, outfile, indent=4, ensure_ascii=False)
    
data = rqs.get('https://ge.globo.com/')
scraptime = datetime.now()
soup = bsp(data.text, 'html.parser')

scrapped_data = {
        'full_content': [span.text for span in soup.find_all('div', {'class':'feed-post-body'})],
        'headers':[span.text for span in soup.find_all('div', {'class': 'feed-post-header with-post-chapeu'})],
        'title':[span.text for span in soup.find_all('div', {'class': 'feed-post-body-title '
                                                                         'gui-color-primary gui-color-hover'})],
        'review':[span.text for span in soup.find_all('div', {'class': 'feed-post-body-resumo'})],
        'related':[span.text for span in soup.find_all('div', {'class': 'bstn-fd-relatedtext'})],
        'feed_time':[span.text for span in soup.find_all('div', {'class': 'feed-post-metadata'})],
        'scraptime': scraptime.strftime('%d/%m/%Y %H:%M')

    }

print(json.dumps(scrapped_data, indent=4, ensure_ascii=False))
aux = scraptime.strftime('%d-%m-%Y %H-%M')
with open(f"json/outputge({aux}).json", 'w') as outfile:
    json.dump(scrapped_data, outfile, indent=4, ensure_ascii=False)
