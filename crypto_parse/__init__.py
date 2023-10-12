from .parser import get_coin_ranks
import json


class tickers:
    path_of_tickers = "C:\\openbot\\crypto_parse\\tickers.json"

    @classmethod
    def get_tickers(cls):
        with open(cls.path_of_tickers, 'r', encoding='utf-8') as file:
            _tickers = {_ticker for _ticker in json.loads(file.read())}
        
        return _tickers

    @classmethod
    def get_valid_coin_info(cls) -> list:
        _tickers = cls.get_tickers()
        _coins = get_coin_ranks(_tickers)
        USDT = float(cls.get_USDT(_coins).get('price'))

        for _coin in _coins:
            market_cap = int(_coin.get('marketCap'))
            _coin['marketCap'] = cls.get_valid_marketcap(market_cap)


            if _coin.get('ticker') == 'USDT':
                _coin['price'] = cls.get_valid_USDT_price(USDT)
                continue

            price = float(_coin.get('price'))
            _coin['price'] = cls.get_valid_USDT_price(price, USDT)

        return _coins
            
    
    @staticmethod
    def get_valid_marketcap(_mc: int) -> str:
        if _mc < 1_000_000:
            return f"${_mc}"
        elif _mc < 1_000_000_000:
            return f"${round(_mc / 1_000_000, 3)}млн"
        else:
            return f"${round(_mc / 1_000_000_000, 3)}млрд"
    
    @staticmethod
    def get_valid_USDT_price(_price: float, _USDT: float | None = None) -> str:
        _res: str

        if _USDT:
            _price /= _USDT
        
        if _price < 500:
            _res = f"{round(_price, 10)}"
        else:
            _res = f"{round(_price, 6)}"
        
        if _USDT:
            _res += ' USDT'
        else:
            _res = '$' + _res
        
        return _res

    
    @staticmethod
    def get_USDT(_coins: list) -> dict:
        for _coin in _coins:
            if _coin.get('ticker') != 'USDT':
                continue

            return _coin
