#!/usr/bin/python3
"""get top 10 posts"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent":  'Chrome/111.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"][:10]
        for post in posts:
            print(post['data']['title'])
    else:
        print('None')
