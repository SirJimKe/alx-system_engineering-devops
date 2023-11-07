#!/usr/bin/python3
"""
Queries Reddit API and returns number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:reddit.api:v1.0.0"
        }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        results = response.json().get("data")
        subscribers_count = results.get("subscribers")
        return subscribers_count
    else:
        return 0
