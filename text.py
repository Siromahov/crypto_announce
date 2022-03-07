import get_price
import fell_or_raised

text = (f"The current price of Litecoin is {get_price.rounded_LTC}$\n"
        f"{fell_or_raised.LTC_fell_or_raised}\n\n"
        f"The current price of Bitcoin is {get_price.rounded_BTC}$\n"
        f"{fell_or_raised.BTC_fell_or_raised}\n\n"
        f"The current price of Ethereum is {get_price.rounded_ETH}$\n"
        f"{fell_or_raised.ETH_fell_or_raised}")
