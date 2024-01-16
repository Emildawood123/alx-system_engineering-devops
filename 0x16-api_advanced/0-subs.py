#!/usr/bin/python3
"""function return from subreddit api"""
import requests


def number_of_subscribers(subreddit):
    """get number of subscribers from api"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    req = requests.get(url, headers={'User-Agent': 'MyPythonScript/1.0'})
    if req.status_code != 200:
        return 0
    try:
        return req.json().get('data').get('subscribers')
    except Exception:
        return 0
