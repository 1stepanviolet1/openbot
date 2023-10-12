import requests as req
import json


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "x-access-token": "coinrankingb639c5d02c626bc9037980ccd4888a9120df7a039f7a08fc"
}

URL = "https://api.coinranking.com/v2/coins"


def get_coin_ranks(_tickers: set) -> list:        
    resp = req.get(URL, headers=headers)
    coins: list = json.loads(resp.text).get('data').get('coins')
    
    coin_ranking: list = []
    for coin in coins:
        ticker = coin.get('symbol')
        if ticker not in _tickers:
            continue
        
        coin_info = {
            "ticker": ticker,
            "marketCap": coin.get('marketCap'),
            "price": coin.get('price')
        }
        coin_ranking.append(coin_info)
    
    return coin_ranking


if __name__ == '__main__':
    print(get_coin_ranks({'BTC', 'ETH'}))
