from url_hurl import gen_from_urls
import pprint

urls = ('http://google.com', 'http://yahoo.com', 'http://facebook.com')

for resp_len, status, url in gen_from_urls(urls):
    print(resp_len, '->', status, '->', url)

urls_res = {url: size for size, _, url in gen_from_urls(urls)}
# demonstrates that the generator function can be used within dict comp 
pprint.pprint(urls_res)
