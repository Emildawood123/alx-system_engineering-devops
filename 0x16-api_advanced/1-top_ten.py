#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def top_ten(subreddit):
    """get number of subscribers from api"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    h = {'User-Agent': 'MyPythonScript/1.0'}
    req = requests.get(url, headers=h)
    if req.status_code != 200:
        return 0
    if (req.json().get('data').get('subscribers') is not None):
        hot = req.json().get('data').get('children')
        if hot is None:
            return print(None)
        for hotta in hot:
            print(hotta.get('data'.get('title')))
    else:
        return print(None)
