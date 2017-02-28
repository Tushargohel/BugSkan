import urllib.parse
c = input(" 1. Encoding	2. Decoding")
if c == '1':
    url = input("enter url:  ")
    en_url = urllib.parse.quote_plus(url)
    print(en_url)
else:
    url = input("enter url:  ")
    de_url = urllib.parse.unquote_plus(url)
    print(de_url)
