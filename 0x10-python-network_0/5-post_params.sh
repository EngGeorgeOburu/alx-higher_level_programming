#!/bin/bash
# Bash script that takes URL snding a POST request to the passed URL
curl -s -X POST -d "email=test@gmail.comsubject&subject=I will always be here for PLD" "$1"
