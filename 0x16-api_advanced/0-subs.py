#!/usr/bin/python3
"""returns the number of subscribers"""


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns
        the number of subscribers
    """
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    response = requests.get(url, headers=headers)
    if response.status_code >= 300:
        return 0
    data = response.json()
    return data.get('data').get('subscribers')
