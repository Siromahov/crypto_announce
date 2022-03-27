from scrape_and_send import price_get

# HOT percentage check
HOT_fell_or_raised = price_get.HOT_percentage
if HOT_fell_or_raised == "+":
    HOT_fell_or_raised = f"Holo raised by {price_get.HOT_percentage}"
else:
    HOT_fell_or_raised = f"Holo fell by {price_get.HOT_percentage}"

# LTC percentage check
LTC_fell_or_raised = price_get.LTC_percentage[0]
if LTC_fell_or_raised == "+":
    LTC_fell_or_raised = f"Litecoin raised by {price_get.LTC_percentage}"
else:
    LTC_fell_or_raised = f"Litecoin fell by {price_get.LTC_percentage}"

# BTC percentage check
BTC_fell_or_raised = price_get.BTC_percentage[0]
if BTC_fell_or_raised == "+":
    BTC_fell_or_raised = f"Bitcoin raised by {price_get.BTC_percentage}"
else:
    BTC_fell_or_raised = f"Bitcoin fell by {price_get.BTC_percentage}"

# ETH percentage check
ETH_fell_or_raised = price_get.ETH_percentage[0]
if ETH_fell_or_raised == "+":
    ETH_fell_or_raised = f"Ethereum raised by {price_get.ETH_percentage}"
else:
    ETH_fell_or_raised = f"Ethereum fell by {price_get.ETH_percentage}"
