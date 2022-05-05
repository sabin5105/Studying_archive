import ccxt
from datetime import datetime

binance = ccxt.binance()
# markets = binance.fetch_tickers()
# print(markets.keys())
ticker = binance.fetch_ticker('ETH/BTC')
print(ticker['open'], ticker['high'], ticker['low'], ticker['close'])

ohlcvs = binance.fetch_ohlcv('ETH/BTC')
for ohlc in ohlcvs:
    print(datetime.fromtimestamp(ohlc[0]/1000).strftime('%Y-%m-%d %H:%M:%S'))

# asks : 매도호가, bids : 매수호가 | orderbook : 가격/수량
orderbook = binance.fetch_order_book('ETH/BTC')
for ask in orderbook['asks']:
    print(ask[0], ask[1])