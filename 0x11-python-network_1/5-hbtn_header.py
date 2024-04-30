#!/usr/bin/python3
"""
Python script taking in a url and sending a request to the url
and displayingthe value
"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
