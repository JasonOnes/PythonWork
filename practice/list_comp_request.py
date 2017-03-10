"""first trying with listcomp"""


import requests

urls = ('http://google.com', 'http://twitter.com', 'http://imgur.com')

for resp in [requests.get(url) for url in urls]:
    print(len(resp.content), '->', resp.status_code, '->', resp.url)


""" demonstrates how long listcomp process takes since it must process in entirety"""
