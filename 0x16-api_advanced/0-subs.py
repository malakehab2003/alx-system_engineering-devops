#!/usr/bin/python3
"""get subreddits of sent reddit"""
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        no_of_subs = data['data']['subscribers']
        return (no_of_subs)
    else:
        return (0)
