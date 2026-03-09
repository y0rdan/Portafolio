import requests
import sys
from pwn import *



url = "http://testphp.vulnweb.com"
data = {"username": "jhon", "password": "pass123"}



r = requests.get(url, data=data, timeout=5, allow_redirects=True)


try:
    r.raise_for_status()

    print(r.text)
    print(r.status_code)
    print(r.encoding)
except requests.exceptions.HTTPError as e:
    print(e)


rp = requests.post(url, data=data, timeout=5, allow_redirects=True)
print(rp.text)
print(rp.status_code)
print(rp.encoding)

print(rp.cookies)
print(rp.headers)
