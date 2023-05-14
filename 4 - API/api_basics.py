# requests - Get na API
# json - Interpretar esse arquivo
import requests, json

# Get = Get Request from the API ( get -> Traz um JSON)
api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=ac86e638-a9c2-4853-80a1-08f1efa726b5")

# Usa módulo de JSON para ler o JSON que recebemos da API
api_content = json.loads(api_request.content)

# Olhar o Arquivo JSON para entender ( dicionário de Listas ):
# Section of Dictionary "data", Index of list "0", Atributo "symbol"
print("Data/0/Symbol -",api_content["data"][0]["symbol"])
print("Data/0/Quote/USD/Price -","{0:.2f}".format(api_content["data"][0]["quote"]["USD"]["price"]))
print("---------------")

# Printing All
for i in range(0,5):
    print(api_content["data"][i]["symbol"])
    print("{0:.2f}".format(api_content["data"][i]["quote"]["USD"]["price"]))
    print("---------------")

# Getting Just Specific Ones
print("Specific Ones: \n---------------")
coins = ["BTC", "BNB"]

for i in range(0,5):
    for coin in coins:
        if api_content["data"][i]["symbol"] == coin:
            print(api_content["data"][i]["symbol"])
            print("{0:.2f}".format(api_content["data"][i]["quote"]["USD"]["price"]))
            print("---------------")
