#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <username> <personal_access_token>")
    else:
        username = sys.argv[1]
        pat = sys.argv[2]
        api_url = 'https://api.github.com/user'
        headers = {
            'Authorization': 'Basic ' + (username + ':' + pat).encode('utf-8')
            .decode('base64')
        }
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data.get('id')
            print("GitHub ID:", user_id)
        else:
            print("Error: Unable to fetch GitHub ID. Status code: {}"
                  .format(response.status_code))
