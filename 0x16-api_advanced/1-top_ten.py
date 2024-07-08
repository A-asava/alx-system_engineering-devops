#!/usr/bin/python3
"""defines a module"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the
        titles of the first 10 hot posts listed for a given subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    response = requests.get(url, headers=headers, allow_redirects=False).json()
    top_ten = response.get('data', {}).get('children', [])
    if not top_ten:
        print("None")
    for top in top_ten:
        print(top.get('data').get('title'))
