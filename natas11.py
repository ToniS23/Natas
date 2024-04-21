#!/usr/bin/env python

import requests
import re
from urllib.parse import unquote
import base64

username = 'natas11'
password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'

url = 'http://%s.natas.labs.overthewire.org/' % username

#PHP XOR


session = requests.session()

response = session.get(url, auth = (username, password))
#response = session.get(url + "index.php?page=../../../../proc/self/cmdline", auth = (username, password)) #see how program is run
content = response.text
unquote = unquote(session.cookies['data'])
decodeb64 = base64.b64decode(unquote)

#print(content)
print(decodeb64)
#print(re.findall('<!--The password for natas3 is (.*) -->', content))