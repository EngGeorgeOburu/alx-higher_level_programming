#!/usr/python3
"""
Scripot taking url and email addreess
"""

import requests
from sys import argv


if __nme__ == '__main__':
    payload = {'email':argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
