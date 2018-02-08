# -*- coding:utf-8 -*-

import configparser
import urllib
import oauth2 as oauth

def oauth_request(url, key, secret, http_method='GET', post=body='', http_headers=None):
    
    config = configparser.ConfigParser()
    config.read('twitter.ini')
    
    consumer = oauth2.Consumer(key=config['authentication']['consumer_key'], secret=config['authentication']['consumer_secret'])
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    response_page, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
    return content

if __name__ == '__main__':
    home_timeline = oauth_req( 'https://api.twitter.com/1.1/statuses/home_timeline.json', 'abcdefg', 'hijklmnop' )
    print(home_timeline)
