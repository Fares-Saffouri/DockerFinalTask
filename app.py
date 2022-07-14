from flask import Flask
import requests
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

# return current bitcoin price function
def getCurrnetBitCoinPrice(): 
    # save in the variable BitCoin_Current_Price the current bitcoin price.
    # this request.get returns in json format a single object and the ['USD'] get the value(price).
    BitCoin_Current_Price = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD').json()['USD']
    return BitCoin_Current_Price

# return average of bitcoin price for the last 10 minutes function
def getAverageBitCoinPrice():
    # save in the variable BitCoin_EveryMinute_Price 10 objects in json format
    # each object contains info about bitcoin for a single minute
    BitCoin_EveryMinute_Price = requests.get('https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=9').json()['Data']['Data']
    sum=0
    for everyminute in BitCoin_EveryMinute_Price:
        # everyminute['close'] its the price for minute
        sum+=everyminute['close']
    return (sum/10)

@app.route("/")
def home():
    # True loop used for getting the price almost every second
    while True:
        # I limited the price for 4 decimal
        price = float("{:.4f}".format(getCurrnetBitCoinPrice()))
        average_price = float("{:.4f}".format(getAverageBitCoinPrice()))
        # save it in redis
        cache.set('currentPrice', price)
        cache.set('averagePrice', average_price)

        # I used this return with refresh to update the content in page without clicking refresh each time
        return """
        <meta http-equiv="refresh" content="1" /><h1>Current BitCoin Price is: {}$</h1><br> <h1>Average BitCoin Price Last 10 Minutes: 
        {}$ </h1>""".format(price,average_price)

