#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return 0

    try:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    except KeyError:
        return 0

# Test cases
print(number_of_subscribers("existing_subreddit"))  # Output: OK
print(number_of_subscribers("nonexisting_subreddit"))  # Output: OK
