from celery import shared_task
from .models import Crypto, Price
from .utils import get_current_price
from concurrent.futures import ThreadPoolExecutor

def update_crypto_price(crypto):
    """
    Update the price of a given cryptocurrency.
    
    Args:
        crypto (Crypto): The cryptocurrency object to update the price for.
    """
    # Get the current price of the cryptocurrency
    current_price = get_current_price(crypto.symbol)
    if current_price is None:
        return
    
    # Create a new Price record for the cryptocurrency
    Price.objects.create(symbol=crypto, price=current_price)

def get_all_prices(cryptos: list[Crypto]):
    """
    Update prices for all cryptocurrencies using a thread pool.
    
    Args:
        cryptos (list[Crypto]): A list of cryptocurrency objects to update prices for.
    """
    # Use a ThreadPoolExecutor to update prices concurrently
    with ThreadPoolExecutor(max_workers=2) as executor:
        for _ in executor.map(update_crypto_price, cryptos):
            pass

@shared_task()
def update_prices():
    """
    Celery task to update prices for all cryptocurrencies.
    """
    # Get all cryptocurrency objects and update their prices
    get_all_prices(Crypto.objects.all())
