from winotify import Notification, audio
import time, bs4, pandas, requests

app_id = ""
title = ""
msg = ""
duration = "long"

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given link.

url = "https://www.eugjams.com/"
r = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(r.content)
data = []

shows = soup.find_all("li", oid="15533")

print(shows[6])

toast = Notification(app_id="EugJams.com",
                     title=title,
                     msg=msg,
                     duration=duration)


toast.show()