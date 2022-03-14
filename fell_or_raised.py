import get_price


# HOT percentage check
HOT_fell_or_raised = get_price.HOT_percentage[0]
if HOT_fell_or_raised == "+":
    HOT_fell_or_raised = f"Holo raised by {get_price.HOT_percentage}"
else:
    HOT_fell_or_raised = f"Holo fell by {get_price.HOT_percentage}"

# LTC percentage check
LTC_fell_or_raised = get_price.LTC_percentage[0]
if LTC_fell_or_raised == "+":
    LTC_fell_or_raised = f"Litecoin raised by {get_price.LTC_percentage}"
else:
    LTC_fell_or_raised = f"Litecoin fell by {get_price.LTC_percentage}"

# BTC percentage check
BTC_fell_or_raised = get_price.BTC_percentage[0]
if BTC_fell_or_raised == "+":
    BTC_fell_or_raised = f"Bitcoin raised by {get_price.BTC_percentage}"
else:
    BTC_fell_or_raised = f"Bitcoin fell by {get_price.BTC_percentage}"

# ETH percentage check
ETH_fell_or_raised = get_price.ETH_percentage[0]
if ETH_fell_or_raised == "+":
    ETH_fell_or_raised = f"Ethereum raised by {get_price.ETH_percentage}"
else:
    ETH_fell_or_raised = f"Ethereum fell by {get_price.ETH_percentage}"
