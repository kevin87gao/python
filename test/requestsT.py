#!/usr/bin/env python
# coding=utf-8

import requests

url = 'http://www.baidu.com'

rsp = requests.get(url)
rsp.encoding = 'utf-8'

print(rsp.text)
