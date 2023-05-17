import requests, json, sqlite3
from tkinter import *

# Instance to use the tkinter (GUI module)
tk_inst = Tk()

# Window Title
tk_inst.title("Crypto GUI")

# Icon ( MUST BE .ICO)
tk_inst.iconbitmap('Img/Cryp.ico')

# Connect with database
con = sqlite3.connect("coin.db")
cursor = con.cursor()

# Create table  ( sql lite toda primary key é autoincrement )
cursor.execute("create table if not exists coin(id integer primary key, symbol text, amount integer, price real)")
con.commit()

# Fill the table ( com os dados da carteira - não vamos usar aquela lista ) 
# cursor.execute("insert into coin (symbol, amount, price) values('BTC', 2, 3000)")
# con.commit()
# cursor.execute("insert into coin (symbol, amount, price) values('ETH', 6, 1000)")
# con.commit()
# cursor.execute("insert into coin (symbol, amount, price) values('BNB', 22, 2460)")
# con.commit()
# cursor.execute("insert into coin (symbol, amount, price) values('SOL', 8, 8)")
# con.commit()

# Function to define Font Color ( Red or Green)
def font_color(amount):
    if amount >= 0:
        return "#3ECE4C"
    return "#D13838"

# Function to make the header of the table:
def table_header():
    id = Label(tk_inst,text="Id", bg="#1E1E1E", fg="white", font="Lato 11 bold", padx="5", pady="5", borderwidth=2, relief="groove")       # Label
    id.grid(row=0,column=0, sticky=N+S+E+W) 

    symb = Label(tk_inst,text="Coin", bg="#1E1E1E", fg="white", font="Lato 11 bold", padx="5", pady="5", borderwidth=2, relief="groove")       # Label
    symb.grid(row=0,column=1, sticky=N+S+E+W)                       # Label Position

    priceb = Label(tk_inst,text="Price Bought", bg="#1E1E1E", fg="white", font="Lato 11 bold", padx="5", pady="5", borderwidth=2, relief="groove")    
    priceb.grid(row=0,column=2, sticky=N+S+E+W)            

    units = Label(tk_inst,text="Units Owned", bg="#1E1E1E", fg="white", font="Lato 11 bold", padx="5", pady="5", borderwidth=2, relief="groove")    
    units.grid(row=0,column=3, sticky=N+S+E+W)           

    totalp = Label(tk_inst,text="Total Paid", bg="#1E1E1E", fg="white", font="Lato 11 bold", padx="5", pady="5", borderwidth=2, relief="groove")    
    totalp.grid(row=0,column=4, sticky=N+S+E+W)        

    pricen = Label(tk_inst,text="Price Now", bg="#1E1E1E", fg="white", font="Lato 11 bold", padx="5", pady="5", borderwidth=2, relief="groove")    
    pricen.grid(row=0,column=5, sticky=N+S+E+W)  

    plc = Label(tk_inst,text="P/L per Coin", bg="#1E1E1E", fg="white", font="Lato 11 bold", padx="5", pady="5", borderwidth=2, relief="groove")    
    plc.grid(row=0,column=6, sticky=N+S+E+W)           

    totalpl = Label(tk_inst,text="Total P/L on this", bg="#1E1E1E", fg="white", font="Lato 11 bold", padx="5", pady="5", borderwidth=2, relief="groove")    
    totalpl.grid(row=0,column=7, sticky=N+S+E+W)   

# Function to call the API to get data just when needed
def wallet():

    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=ac86e638-a9c2-4853-80a1-08f1efa726b5")

    api_content = json.loads(api_request.content)

    print("U P D A T E")

    # Fetching Data from the table
    cursor.execute("select * from coin")
    coins = cursor.fetchall()   # A list of TUPLES
    print(coins)

    # Row Number
    row = 1

    # Total PL
    balance = 0

    # Getting Just Specific Ones ( the ones on the db - my wallet)
    for i in range(0,10):
        for coin in coins:
            # Como é uma lista de tuplas, acessamos assim: coin[coluna da tupla]
            if api_content["data"][i]["symbol"] == coin[1]:
                total_paid = coin[3]*coin[2]
                current_value = api_content["data"][i]["quote"]["USD"]["price"]
                pl_percoin = api_content["data"][i]["quote"]["USD"]["price"] - coin[3] 
                total_pl = pl_percoin * coin[2]   # Total PL of this coin

                balance += total_pl

                # Show on GUI
                id = Label(tk_inst,text=coin[0], bg="#FFD73A", fg="black", font="Lato 12", padx="5", pady="5", borderwidth=2, relief="groove")       
                id.grid(row=row,column=0, sticky=N+S+E+W)

                symb = Label(tk_inst,text=api_content["data"][i]["symbol"], bg="#1066AA", fg="white", font="Lato 12", padx="5", pady="5", borderwidth=2, relief="groove")       
                symb.grid(row=row,column=1, sticky=N+S+E+W)                       

                priceb = Label(tk_inst,text="{0:.2f}".format(coin[3]), bg="#FFD73A", fg="black", font="Lato 12", padx="5", pady="5", borderwidth=2, relief="groove")  
                priceb.grid(row=row,column=2, sticky=N+S+E+W)            

                units = Label(tk_inst,text=coin[2], bg="#1066AA", fg="white", font="Lato 12", padx="5", pady="5", borderwidth=2, relief="groove")    
                units.grid(row=row,column=3, sticky=N+S+E+W)           

                totalp = Label(tk_inst,text="{0:.2f}".format(total_paid), bg="#FFD73A", fg="black", font="Lato 12", padx="5", pady="5", borderwidth=2, relief="groove")    
                totalp.grid(row=row,column=4, sticky=N+S+E+W)        

                pricen = Label(tk_inst,text="{0:.2f}".format(current_value), bg="#1066AA", fg="white", font="Lato 12", padx="5", pady="5", borderwidth=2, relief="groove")    
                pricen.grid(row=row,column=5, sticky=N+S+E+W)  

                plc = Label(tk_inst,text="{0:.2f}".format(pl_percoin), bg="#FFD73A", fg="black", font="Lato 12", padx="5", pady="5", borderwidth=2, relief="groove")    
                plc.grid(row=row,column=6, sticky=N+S+E+W)           

                totalpl = Label(tk_inst,text="{0:.2f}".format(total_pl), bg="#1066AA", fg="white", font="Lato 12", padx="5", pady="5", borderwidth=2, relief="groove")   
                totalpl.grid(row=row,column=7, sticky=N+S+E+W) 

                # Increment row
                row += 1

    # Label do BALANCE ( PROFIT = GREEN , LOSS = RED)
    name = Label(tk_inst,text="{0:.2f}".format(balance), bg=font_color(balance), fg="black", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")   
    name.grid(row=row,column=7, sticky=N+S+E+W) 

    # Empty the API
    api_content = ""

    # Botão de Update ( faz um "refresh" nos dados )                    # SEM "()" aqui
    name = Button(tk_inst,text="Update", bg="#1E1E1E", fg="White",command=wallet, font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")   
    name.grid(row=row + 1,column=7, sticky=N+S+E+W)

# Create the header
table_header()

# Call Function
wallet()  

# Fecha o Main loop
tk_inst.mainloop()

# Fecha Conexão
cursor.close()
con.close()
