#!/usr/bin/python3

""" Module defines number_of_subscribers """


import requests


def top_ten(subreddit):
    """ Print the titles of the first 10 hot posts
        listed  for a given subreddit
        Args:
            subreddit: The query string
    """

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "top_ten/1.0 by Francis(Abstrat22)"}
    try:
        response = requests.get(url, headers=headers,
                                params={"limit": 10}, allow_redirects=False)
        data = response.json()["data"]
        [print(title["data"]["title"]) for title in data["children"]]
    except (requests.exceptions.RequestException, KeyError):
        print("None")
