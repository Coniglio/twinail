# -*-p coding:utf-8 -*-

from flask import Flask
from flask_cors import CORS
import ConfigParser
import urllib
import oauth2 as oauth

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins":"*"}})

@app.route("/")
def oauth_request():
    
    config = ConfigParser.ConfigParser()
    config.read('twitter.ini')
    
    consumer = oauth.Consumer(key=config.get("authentication", "consumer_key"), secret=config.get("authentication", "consumer_secret"))
    token = oauth.Token(key='', secret='')
    client = oauth.Client(consumer, token)
    response_page, content = client.request('https://api.twitter.com/1.1/favorites/list.json?count=200', method="GET", body="", headers=None)
    return content

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

