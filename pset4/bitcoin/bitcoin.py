import sys
import requests

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    n = float(sys.argv[1].rstrip())
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)
else:
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        pass
    else:
        rate = float(response.json()["bpi"]["USD"]["rate_float"])
        amount = rate * n
        print(f"${amount:,.4f}")