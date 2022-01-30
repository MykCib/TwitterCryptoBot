from requests import Request, Session
import requests
from datetime import datetime
import json
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import tweepy
import glob, random

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
'start':'1',
'limit':'100'
}
headers = {
'Accepts': 'application/json',
'X-CMC_PRO_API_KEY': '****',    # api key hidden
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

up = -100
name = "nothing"
short = "nothing"
for i in change_list:
    if i[2] > up:
        up = i[2]
        name = i[0]
        short = i[1]
        price = i[3]

rounded = round(up,2)
change =  str(rounded)

# api keys hidden
consumer_key = '****'
consumer_secret = '****'
access_token = '****'
access_token_secret = '****'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

file_path_type = ["/memes/*.jpg"]
images = glob.glob(random.choice(file_path_type))
randoms = random.choice(images)

media = api.media_upload(randoms)

name = name.replace(" ", "")

tweet_1 = "🩸Crypto market is down🩸 \n \nNo gainers among the top 100 cryptocurrencies in the past 24 hours"
tweet_2 = 'The top performing cryptocurrency among the top 100 in the past 24 hours 📈 \n \n🔥 #%s ( $%s ) \n⬆️ It is up by %s%% \n💵 Current price: %s USD' % (name, short,change,price)

if up < 0:
    api.update_status(tweet_1)
else:
    api.update_status(status=tweet_2, media_ids=[media.media_id])


# another tweet starts here #

url_1 = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH&tsyms=USD&api_key={****} " # api key hidden

response_1 = requests.request("GET", url_1)

json_1 = response_1.json()

raw_data = (json_1['RAW'])

btc_data = (raw_data['BTC'])

btc_usd = (btc_data['USD'])

btc_price = (btc_usd['PRICE'])

btc_price_str = str(btc_price)

eth_data = (raw_data['ETH'])

eth_usd = (eth_data['USD'])

eth_price = (eth_usd['PRICE'])

eth_price_str = str(eth_price)

now = datetime.now()

today =('%04d-%02d-%02d' %(now.year, now.month, now.day))

if now.year == 2021:
    url_2 = "https://min-api.cryptocompare.com/data/pricehistorical?fsym=BTC&tsyms=USD&ts=1609459260&api_key={****}"    # api key hidden
    url_3 = "https://min-api.cryptocompare.com/data/pricehistorical?fsym=ETH&tsyms=USD&ts=1609459260&api_key={****}"    # api key hidden


    response_2 = requests.request("GET", url_2)
    response_3 = requests.request("GET", url_3)

    json_2 = response_2.json()
    json_3 = response_3.json()

elif now.year == 2022:
    url_2 = "https://min-api.cryptocompare.com/data/pricehistorical?fsym=BTC&tsyms=USD&ts=1640995260&api_key={****}"    # api key hidden
    url_3 = "https://min-api.cryptocompare.com/data/pricehistorical?fsym=ETH&tsyms=USD&ts=1640995260&api_key={****}"    # api key hidden

    response_2 = requests.request("GET", url_2)
    response_3 = requests.request("GET", url_3)

    json_2 = response_2.json()
    json_3 = response_3.json()

btc_h1 = json_2['BTC']
btc_open = btc_h1['USD']

eth_h1 = json_3['ETH']
eth_open = eth_h1['USD']

btc_open_str = str(btc_open)
eth_open_str = str(eth_open)

#[(New Price - Old Price)/Old Price] * 100

btc_precent = ((btc_price - btc_open) / btc_open) * 100
eth_precent = ((eth_price - eth_open) / eth_open) * 100

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

day = days_between("2021-01-01",today)

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
numbers = [ordinal(n) for n in range(1,366)]

this_day =numbers[day - 1]

if now.day == 1 and now.month == 1:
    this_day = "1st"

#tweet_1 = "📊 It is %s day of %d.\n" %(this_day,now.year)

#btc_head = "\n#Bitcoin $BTC"
#btc_open_price = "\n⬅️ Year open price: %s USD" % (btc_open_str)
#btc_current_price = "\n➡️ Current price: %s USD" % (btc_price_str)
#btcup ="\n📈 Up: %d%%" % (btc_precent)
#btcdown = "\n📉 Down: %d%%" % (btc_precent)

#eth_head = "\n\n#Ethereum $ETH"
#eth_open_price = "\n⬅️ Year open price: %s USD" % (eth_open_str)
#eth_current_price = "\n➡️ Current price: %s USD" % (eth_price_str)
#ethup ="\n📈 Up: %d%%" % (eth_precent)
#ethdown = "\n📉 Down: %d%%" % (eth_precent)

btc_eth_up = ("📊 It is %s day of %d.\n\n#Bitcoin $BTC\n⬅️ Year open price: %s USD\n➡️ Current price: %s USD\n📈 Up: %d%%\n\n#Ethereum $ETH\n⬅️ Year open price: %s USD\n➡️ Current price: %s USD\n📈 Up: %d%%") %(this_day,now.year,btc_open_str,btc_price_str,btc_precent,eth_open_str,eth_price_str,eth_precent)

btc_up_eth_down = ("📊 It is %s day of %d.\n\n#Bitcoin $BTC\n⬅️ Year open price: %s USD\n➡️ Current price: %s USD\n📈 Up: %d%%\n\n#Ethereum $ETH\n⬅️ Year open price: %s USD\n➡️ Current price: %s USD\n📉 Down: %d%%") %(this_day,now.year,btc_open_str,btc_price_str,btc_precent,eth_open_str,eth_price_str,eth_precent)

btc_down_eth_down = ("📊 It is %s day of %d.\n\n#Bitcoin $BTC\n⬅️ Year open price: %s USD\n➡️ Current price: %s USD\n📉 Down: %d%%\n\n#Ethereum $ETH\n⬅️ Year open price: %s USD\n➡️ Current price: %s USD\n📉 Down: %d%%") %(this_day,now.year,btc_open_str,btc_price_str,btc_precent,eth_open_str,eth_price_str,eth_precent)

btc_down_eth_up = ("📊 It is %s day of %d.\n\n#Bitcoin $BTC\n⬅️ Year open price: %s USD\n➡️ Current price: %s USD\n📉 Down: %d%%\n\n#Ethereum $ETH\n⬅️ Year open price: %s USD\n➡️ Current price: %s USD\n📈 Up: %d%%") %(this_day,now.year,btc_open_str,btc_price_str,btc_precent,eth_open_str,eth_price_str,eth_precent)


if btc_precent > 0 and eth_precent > 0:
    api.update_status(btc_eth_up)
elif btc_precent > 0 and eth_precent < 0:
    api.update_status(btc_up_eth_down)
elif btc_precent < 0 and eth_precent < 0:
    api.update_status(btc_down_eth_down)
elif btc_precent < 0 and eth_precent > 0:
    api.update_status(btc_down_eth_up)
