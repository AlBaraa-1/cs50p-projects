import sys
import requests
import json

def main():
    btc = get_btc_amount()
    price = getPrice()

    #get the toal value of bitcoin in USD
    total = btc * price

    #format the output to 4 decimal places
    print(f"${total:,.4f}")

def getPrice():
    #define the url for the API
    url = "https://api.coincap.io/v2/assets/bitcoin"
    headers = {
        "Authorization": "Bearer 29c8f97ff7d4e48c39c0eaf0f3f1dc03468c803f5a347217503a2fc29b0a305f"
    }

    #make a request to the API and get the response
    response = requests.get(url, headers=headers)  
    data = response.json()

    #return the price of bitcoin in USD
    return float(data["data"]["priceUsd"])

def get_btc_amount():
    try:
        #check if the command line argument is a number
        if len(sys.argv) ==2:

            #convert the command line argument to a float and return it
            btcAmount = float(sys.argv[1])
            return btcAmount
        
        #if no arguments are passed exit with an error message
        elif len(sys.argv) == 1:
            sys.exit("Missing command-line argument")
            
        else:
            sys.exit("Missing command-line argument")

    except ValueError:
        sys.exit("Command-line argument is not a number")


if __name__ == "__main__":
    main()