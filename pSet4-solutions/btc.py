# take a lil AI assist on this one for getting information with usage of json library


import json
import requests
import sys

#for live btc value
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = response.json()

'''data = {
    "bpi": {
        "USD": {
            "rate_float": 59466.3685
        }
    }
}'''

try:
    amount = float(sys.argv[1])

    bitcoin_rate = data['bpi']['USD']['rate_float']

    bitcoin_amount = amount * bitcoin_rate

    print(f"${amount:.2f} is equal to {bitcoin_amount:.3f} Bitcoin")

except IndexError:
    print("Error: Please provide an amount as a command-line argument.")
    sys.exit(1)
except ValueError:
    print("Error: Please provide a valid number as the argument.")
    sys.exit(1)
except KeyError:
    print("Error: Unable to parse Bitcoin price data.")
    sys.exit(1)

