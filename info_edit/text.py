from scrape_and_send import price_get
from info_edit import fell_or_raised, selected_info

text = []

BTC = (f"The current price of Bitcoin is {price_get.rounded_BTC}$\n"
       f"{fell_or_raised.BTC_fell_or_raised}\n\n")
ETH = (f"The current price of Ethereum is {price_get.rounded_ETH}$\n"
       f"{fell_or_raised.ETH_fell_or_raised}\n\n")
LTC = (f"The current price of Litecoin is {price_get.rounded_LTC}$\n"
       f"{fell_or_raised.LTC_fell_or_raised}\n\n")
HOT = (f"The current price of Holo is {price_get.rounded_HOT}$\n"
       f"{fell_or_raised.HOT_fell_or_raised}\n\n")

if 'BTC' in selected_info.selected:
    text.append(BTC)
if 'ETH' in selected_info.selected:
    text.append(ETH)
if 'LTC' in selected_info.selected:
    text.append(LTC)
if 'HOT' in selected_info.selected:
    text.append(HOT)

print("".join(text))
