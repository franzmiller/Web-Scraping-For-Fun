import requests
import bs4
import pandas as pd

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given link.

url = "https://coeapps.eugene-or.gov/EPDDispatchLog/"
r = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(r.content, 'html5lib')

rows = soup.find_all("tr")
for call in rows:
    for item in call.find_all("td"):
        call_time = item[1].string
        dispatch_time = item[2].string
        incident = item[3].string
        disposition = item[4].string
        num = item[5].string
        location = item[6].string
        priority = item[7].string
        case = item[8].string
        print(disposition)
        print(item.prettify())