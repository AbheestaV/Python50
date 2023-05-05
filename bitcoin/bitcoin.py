import json
import requests
import sys


if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o = response.json()
bitcoin = o["bpi"]["USD"]["rate_float"]
print(f"${float(sys.argv[1])*bitcoin:,.4f}")


