""" trying same thing with generator instead of listcomp for speed comparison"""


import requests

urls = ('http://google.com', 'http://youtube.com', 'http://amazon.com')

for resp in (requests.get(url) for url in urls):
    print(len(resp.content), '->', resp.status_code, '->', resp.url)

    #switched () for [] in listcomp
#resp = response
