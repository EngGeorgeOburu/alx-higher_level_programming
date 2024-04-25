#!/bin/bash
# Bash script taking in URL and displaying all HTTP methods
# that the server will accept
curl -sL "$1" | grep "Allow" | cut -d " " -f 2-
