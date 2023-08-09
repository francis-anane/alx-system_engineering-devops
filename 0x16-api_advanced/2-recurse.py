#!/usr/bin/python3

""" Module defines recurse """


import requests


def recurse(subreddit, hot_list=[], count=0, after=""):
    """ Retuen a list containing the titles of all
        hot articles of  a given subreddit
        Args:
            subreddit: The query string
            hot_list: The list to return
            count: counter for items
            after: next item
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "top_ten/1.0 by Francis(Abstrat22)"}

    params = {"limit": 100, "after": after}
    try:
        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        if "data" in data and "children" in data["data"]:
            articles = data["data"]["children"]
            if not articles:
                return None

            titles = [article["data"]["title"] for article in articles]
            hot_list.extend(titles)

            after = data["data"]["after"]
            if after:
                return recurse(subreddit, hot_list,
                               count + len(articles), after)
            else:
                return hot_list
        else:
            return None
    except requests.exceptions.RequestException:
        return None
