#!/usr/bin/env python

import requests
import re

username = 'natas8'
password = 'a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.session()

#first look at the source code and try to figure out what is the order to decode, gl

#response = session.get(url + "index.php?page=../../../../etc/passwd", auth = (username, password))
response = session.post(url,data = {'secret':'oubWYf2kBq', 'submit':'submit'}, auth = (username, password))
#response = session.get(url + "index.php?page=../../../../proc/self/cmdline", auth = (username, password)) #see how program is run
content = response.text

print(content)
#print(re.findall('<!--The password for natas3 is (.*) -->', content))