#!/usr/bin/python
import requests
print(site = requests.get("https://businesscorp.com.br"))
print(site.content)
print(site.headers)
print(site.statuscode)
print(site.headers['server'])
