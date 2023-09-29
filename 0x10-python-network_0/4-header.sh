#!/bin/bash
# Sends a GET request to the provided URL with custom header and displays response body
curl -s -H "X-School-User-Id: 98" "$1"
