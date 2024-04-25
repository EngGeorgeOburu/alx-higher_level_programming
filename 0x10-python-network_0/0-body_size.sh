#!/bin/bash
#Script that takes in URL, and sends a request to that URL
curl -sL "$1" | wc -c
