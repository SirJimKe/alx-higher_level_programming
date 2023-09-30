#!/usr/bin/python3
"""
Holberton school interview challenge
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <repository_name> <owner_name>")
    else:
        repository_name = sys.argv[1]
        owner_name = sys.argv[2]
        api_url = f'https://api.github.com/repos/{owner_name}/{repository_name}/commits'
        response = requests.get(api_url)

        if response.status_code == 200:
            commits = response.json()[:10]
            for commit in commits:
                sha = commit.get('sha')
                author_name = commit.get('commit').get('author').get('name')
                print(f'{sha}: {author_name}')
        else:
            print("Error: Unable to fetch commits. Status code:", response.status_code)
