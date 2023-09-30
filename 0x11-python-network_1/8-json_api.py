#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
"""
import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        response_data = response.json()

        if response_data:
            user_info = response_data[0]
            user_id = user_info.get('id')
            user_name = user_info.get('name')
            print("[{}] {}".format(user_id, user_name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
