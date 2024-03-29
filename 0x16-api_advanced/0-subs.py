#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """get number of subscribers from api"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    h = {'User-Agent': 'cheetahExpert6025'}
    req = requests.get(url, headers=h)
    if req.status_code != 200:
        return 0
    if (req.json().get('data').get('subscribers') is not None):
        return req.json().get('data').get('subscribers')
    else:
        return 0
