#!/bin/bash
# A Bash script that takes in a URL and displays all HTTP methods
curl -s -X OPTIONS "$1" | grep -o "Allow:.*" | sed -E "s/Allow: (.*)/\1/g"
