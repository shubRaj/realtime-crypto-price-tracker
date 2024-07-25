import requests

HEADERs = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.5',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}



def get_current_price(symbol = "BTCUSDT"):
    params = {
    'symbol': symbol,
    }
    response = requests.get('https://api.binance.com/api/v3/ticker/price', params=params, headers=HEADERs)
    if response.status_code != 200:
        return
    return response.json()["price"]
if __name__ == "__main__":
    print(get_current_price())