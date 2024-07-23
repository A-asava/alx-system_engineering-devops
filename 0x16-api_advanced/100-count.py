#!/usr/bin/python3
import requests
import re

def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively fetches posts from Reddit and counts keyword occurrences."""
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    children = data.get('children', [])
    after = data.get('after')

    for post in children:
        title = post['data']['title'].lower()
        for word in counts:
            # Count occurrences of each word using regex
            counts[word] += len(re.findall(rf'\b{re.escape(word)}\b', title))

    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        # Print results sorted by count (descending) and then alphabetically
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word}: {count}")


