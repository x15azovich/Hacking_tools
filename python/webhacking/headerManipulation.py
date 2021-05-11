#!/usr/bin/python
import requests
myheaders={'User-Agent' :'Fake Agent'}
r = requests.get('http://httpbin.org/headers')
print r.url
print r.text
r2 = requests.get('http://httpbin.org/headers', headers=myheaders)
print r2.text

r3= requests.get('http://192.168.141', headers=myheaders)
print r3.text
