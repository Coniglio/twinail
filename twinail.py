# -*- coding:utf-8 -*-

import urllib
import oauth2 as oauth

request_token_url = ''
access_token_url = ''
authenticate_url = ''
callback_url = ''
consumer_key = ''
consumer_secret = ''

def oauth_request(url, key, secret, http_method='GET', post=body='', http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    response_page, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
    return content

if __name__ == '__main__':

    home_timeline = oauth_req( 'https://api.twitter.com/1.1/statuses/home_timeline.json', 'abcdefg', 'hijklmnop' )
    print(home_timeline)
