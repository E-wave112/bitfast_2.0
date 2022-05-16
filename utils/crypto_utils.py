from decouple import config
from coinbase.wallet.client import Client

# define the coinbase python client
client = Client(config("COINBASE_API_KEY"), config("COINBASE_SECRET_KEY"))

# convert scientific notations to decimals
def _to_decimals(std_form):
    return ("%.17f" % std_form).rstrip("0").rstrip(".")


def get_crypto_prices():
    rates = client.get_exchange_rates(currency="USD")
    context = {
        "Bitcoin": _to_decimals(1 / float(rates["rates"]["BTC"])),
        "Ethereum": _to_decimals(1 / float(rates["rates"]["ETH"])),
        "Dogecoin": _to_decimals(1 / float(rates["rates"]["DOGE"])),
        "Solana": _to_decimals(1 / float(rates["rates"]["SOL"])),
        "Shiba": _to_decimals(1 / float(rates["rates"]["SHIB"])),
        "Tether": _to_decimals(1 / float(rates["rates"]["USDT"])),
    }
    
    return {"exchange rates for popular coins": context}
