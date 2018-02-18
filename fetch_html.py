import requests

class fetch_html:

    def __init__(self, url):
        res = requests.get(url)
        res.raise_for_status()
        self.html = res.text
