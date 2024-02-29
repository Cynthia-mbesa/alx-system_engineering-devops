#!/usr/bin/python3
"""Module for task 1"""


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    import requests

    def top_ten(subreddit):
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {"User-Agent": "My-User-Agent"}
        params = {"limit": 10}
        response = requests.get(
                url, headers=headers, params=params, allow_redirects=False
                )

        if response.status_code != 200:
            print(None)
            return

        try:
            data = response.json()
            posts = data["data"]["children"]

            for post in posts:
                print(post["data"]["title"])
        except (KeyError, ValueError):
            print(None)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
