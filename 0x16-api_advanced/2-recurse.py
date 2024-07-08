#!/usr/bin/python3
"""Defining a module"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """recursive function that queries the Reddit API and
        returns a list containing the titles of all hot
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"count": count, "after": after}
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code >= 400:
        return None
    data = response.json()
    hot = hot_list + [post.get('data').get("title")
                      for post in data.get('data').get('children')]
    if not data.get("data").get("after"):
        return hot
    return recurse(subreddit, hot, data.get("data").get("count"),
                   data.get('data').get("after"))
