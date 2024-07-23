#!/usr/bin/python3
"""
queries the top ten hot posts of a given Reddit subreddit.
"""

import requests

def top_ten(subreddit):
    """Print the titles of the top 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            try:
                data = response.json().get('data', {}).get('children', [])
                if not data:
                    print("No posts found.")
                    return
                for post in data:
                    print(post['data']['title'])
            except ValueError:
                print("Error: Could not decode JSON response.")
        else:
            print("None")
    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

