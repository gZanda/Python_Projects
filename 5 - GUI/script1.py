import requests, json
from tkinter import *

# Function to define Font Color ( Red or Green)
def font_color(amount):
    if amount >= 0:
        return "#3ECE4C"
    return "#D13838"

# Function to call the API to get data just when needed
def wallet():

    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=ac86e638-a9c2-4853-80a1-08f1efa726b5")

    api_content = json.loads(api_request.content)

    print("------------------------------")

    # Uma lista com um dicionário dentro ( WALLET )
    coins = [
        {
            "symbol":"BTC",
            "amount_owned": 2,
            "price_per_unit": 3000
        },
        {
            "symbol":"BNB",
            "amount_owned": 22,
            "price_per_unit": 2460
        }
    ]

    # Row Number
    row = 1

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

                # Show on GUI
                name = Label(tk_inst,text=api_content["data"][i]["symbol"], bg="#1066AA", fg="white", font="Lato 12", padx="5", pady="5", borderwidth=2, relief="groove")       
                name.grid(row=row,column=0, sticky=N+S+E+W)                       

                name = Label(tk_inst,text="{0:.2f}".format(coin["price_per_unit"]), bg="#FFD73A", fg="black", font="Lato 12", padx="5", pady="5", borderwidth=2, relief="groove")  
                name.grid(row=row,column=1, sticky=N+S+E+W)            

                name = Label(tk_inst,text=coin["amount_owned"], bg="#1066AA", fg="white", font="Lato 12", padx="5", pady="5", borderwidth=2, relief="groove")    
                name.grid(row=row,column=2, sticky=N+S+E+W)           

                name = Label(tk_inst,text="{0:.2f}".format(total_paid), bg="#FFD73A", fg="black", font="Lato 12", padx="5", pady="5", borderwidth=2, relief="groove")    
                name.grid(row=row,column=3, sticky=N+S+E+W)        

                name = Label(tk_inst,text="{0:.2f}".format(current_value), bg="#1066AA", fg="white", font="Lato 12", padx="5", pady="5", borderwidth=2, relief="groove")    
                name.grid(row=row,column=4, sticky=N+S+E+W)  

                name = Label(tk_inst,text="{0:.2f}".format(pl_percoin), bg="#FFD73A", fg="black", font="Lato 12", padx="5", pady="5", borderwidth=2, relief="groove")    
                name.grid(row=row,column=5, sticky=N+S+E+W)           

                name = Label(tk_inst,text="{0:.2f}".format(total_pl), bg="#1066AA", fg="white", font="Lato 12", padx="5", pady="5", borderwidth=2, relief="groove")   
                name.grid(row=row,column=6, sticky=N+S+E+W) 

                # Increment row
                row = row + 1

    # Label do BALANCE ( PROFIT = GREEN , LOSS = RED)
    name = Label(tk_inst,text="{0:.2f}".format(balance), bg=font_color(balance), fg="black", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")   
    name.grid(row=row,column=6, sticky=N+S+E+W) 

    # Empty the API
    api_content = ""

    # Botão de Update ( faz um "refresh" nos dados )                    # SEM "()" aqui
    name = Button(tk_inst,text="Button", bg="#1E1E1E", fg="White",command=wallet, font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")   
    name.grid(row=row + 1,column=6, sticky=N+S+E+W)

# Instance to use the module
tk_inst = Tk()

# Call Function
wallet()

# Window Title
tk_inst.title("Crypto GUI")

# Icon ( MUST BE .ICO)
tk_inst.iconbitmap('Img/Cryp.ico')

# Faz o "Corpo" da tabela a ser usada
name = Label(tk_inst,text="Coin", bg="#1E1E1E", fg="white", font="Lato 11 bold", padx="5", pady="5", borderwidth=2, relief="groove")       # Label
name.grid(row=0,column=0, sticky=N+S+E+W)                       # Label Position

name = Label(tk_inst,text="Price Bought", bg="#1E1E1E", fg="white", font="Lato 11 bold", padx="5", pady="5", borderwidth=2, relief="groove")    
name.grid(row=0,column=1, sticky=N+S+E+W)            

name = Label(tk_inst,text="Units Owned", bg="#1E1E1E", fg="white", font="Lato 11 bold", padx="5", pady="5", borderwidth=2, relief="groove")    
name.grid(row=0,column=2, sticky=N+S+E+W)           

name = Label(tk_inst,text="Total Paid", bg="#1E1E1E", fg="white", font="Lato 11 bold", padx="5", pady="5", borderwidth=2, relief="groove")    
name.grid(row=0,column=3, sticky=N+S+E+W)        

name = Label(tk_inst,text="Price Now", bg="#1E1E1E", fg="white", font="Lato 11 bold", padx="5", pady="5", borderwidth=2, relief="groove")    
name.grid(row=0,column=4, sticky=N+S+E+W)  

name = Label(tk_inst,text="P/L per Coin", bg="#1E1E1E", fg="white", font="Lato 11 bold", padx="5", pady="5", borderwidth=2, relief="groove")    
name.grid(row=0,column=5, sticky=N+S+E+W)           

name = Label(tk_inst,text="Total P/L on this", bg="#1E1E1E", fg="white", font="Lato 11 bold", padx="5", pady="5", borderwidth=2, relief="groove")    
name.grid(row=0,column=6, sticky=N+S+E+W)     



tk_inst.mainloop()
