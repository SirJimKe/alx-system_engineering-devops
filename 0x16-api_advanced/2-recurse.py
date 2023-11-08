#!/usr/bin/python3
"""
Recursively queries Reddit API
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'linux:api.advanced:v3.0.0'
    }

    if after:
        url += f"?after={after}"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        subreddit_data = response.json()
        for post in subreddit_data['data']['children']:
            hot_list.append(post['data']['title'])
        after = subreddit_data['data']['after']
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
