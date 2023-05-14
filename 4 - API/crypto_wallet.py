# What will we need ? "Coin name" - "Amount Bought" - "Coin Price"
import requests, json

api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=ac86e638-a9c2-4853-80a1-08f1efa726b5")

api_content = json.loads(api_request.content)

print("------------------------------")

# Uma lista com um dicionário dentro
coins = [
    {
        "symbol":"BTC",
        "amount_owned": 2,
        "price_per_unit": 300
    },
    {
        "symbol":"BNB",
        "amount_owned": 22,
        "price_per_unit": 200  
    }
]

# Total PL
balance = 0

# Getting Just Specific Ones
for i in range(0,5):
    for coin in coins:
        if api_content["data"][i]["symbol"] == coin["symbol"]:
            total_paid = coin["price_per_unit"]*coin["amount_owned"]
            current_value = api_content["data"][i]["quote"]["USD"]["price"]
            pl_percoin = api_content["data"][i]["quote"]["USD"]["price"] - coin["price_per_unit"] 
            total_pl = pl_percoin * coin["amount_owned"]   # Total PL of this coin

            balance = balance + total_pl

            print(api_content["data"][i]["name"],":",api_content["data"][i]["symbol"])
            print("Price Bought: {0:.2f}".format(coin["price_per_unit"]))
            print("Number of Coins :",coin["amount_owned"])
            print("Total Paid : {0:.2f}".format(total_paid))
            print("Price Now : {0:.2f}".format(current_value))
            print("Profit/Loss per Coin : {0:.2f}".format(pl_percoin))
            print("Total Profit/Loss on this Coin : {0:.2f}".format(total_pl))
            print("------------------------------")

print("Final Wallet Balance : ${0:.2f}".format(balance))
