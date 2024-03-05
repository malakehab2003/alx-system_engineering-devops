#!/usr/bin/python3
"""recursive get data"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    if not subreddit or not isinstance(subreddit, str):
        return None

    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])

    for child in children:
        title = child.get("data", {}).get("title")
        if title:
            hot_list.append(title)

    after = data.get("after")

    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
