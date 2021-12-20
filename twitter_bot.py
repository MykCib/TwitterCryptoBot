from requests import Request, Session
import time
from datetime import datetime
import sys
import csv
import json
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import tweepy

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
'start':'1',
'limit':'100'
}
headers = {
'Accepts': 'application/json',
'X-CMC_PRO_API_KEY': '****, 
}

session = Session()
session.headers.update(headers)


response = session.get(url, params=parameters)
data = json.loads(response.text)

raw = data['data']

n = 0
change_list = []
names = []
while n < 100:
    a = raw[n]
    b = a["quote"]
    c = b['USD']
    d = c['percent_change_24h']
    e = a['name']
    f = a['symbol']
    g = c['price']
    h = round(g,2)
    j =  str(h)
    two = [e,f,d,j]
    change_list.append(two)
    n += 1

max = -100
name = "nothing"
short = "nothing"
for i in change_list:
    if i[2] > max:
        max = i[2]
        name = i[0]
        short = i[1]
        price = i[3]

rounded = round(max,2)
change =  str(rounded)

consumer_key = '****'           # api keys are hidden
consumer_secret = '****'
access_token = '****'
access_token_secret = '****'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

file_path_type = ["/memes/*.jpg"]                  # change file path
images = glob.glob(random.choice(file_path_type))
randoms = random.choice(images)

media = api.media_upload(randoms)

tweet_1 = "🩸Crypto market is down🩸 \n \nNo gainers among the top 100 cryptocurrencies in the past 24 hours"
tweet_2 = 'The top performing cryptocurrency among the top 100 in the past 24 hours 📈 \n \n🔥 #%s ($%s) \n⬆️ It is up by %s precent \n💵 Current price: %s USD' % (name, short,change,price)

if i[2] > 0:
    api.update_status(tweet_1)
else:
    post_result = api.update_status(status=tweet_2, media_ids=[media.media_id])


