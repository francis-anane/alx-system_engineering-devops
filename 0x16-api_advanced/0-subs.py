#!/usr/bin/python3

""" Module defines number_of_subscribers """


import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscrbers for
       a given subreddit
        Args:
            subreddit: The query string
    """

    # Reddit api url
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "subs/1.0 by Francis(Abstrat22)"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json()
        return data["data"]["subscribers"]
    except (requests.exceptions.RequestException, KeyError):
        return 0
