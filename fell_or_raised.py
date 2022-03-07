import get_price


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
