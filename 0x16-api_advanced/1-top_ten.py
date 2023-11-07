#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "linux:api.advanced:v2.0.0"
        }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        results = response.json()
        for result in results['data']['children']:
            if not result['data']['stickied']:
                print(result['data']['title'])
    else:
        print("None")
