#!/usr/bin/python3
"""
Script fetching data from https://alx-intranet.hbtn.io/status
"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = irllib.request.Request(url)
    with urllib.request.urlopen(request)  as resp:
        print(dict(resp.header).get("X-Request-ID"))
