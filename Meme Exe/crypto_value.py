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

    print("U P D A T E")

    # Row Number
    row = 1

    # Getting Just Specific Ones
    for i in range(0,10):
        current_value = api_content["data"][i]["quote"]["USD"]["price"]

        # Show on GUI
        name = Label(tk_inst,text=api_content["data"][i]["symbol"], bg="#1066AA", fg="white", font="Lato 12", padx="5", pady="5", borderwidth=2, relief="groove")       
        name.grid(row=row,column=0, sticky=N+S+E+W)                                                    

        name = Label(tk_inst,text="{0:.2f}".format(current_value), bg="#FFD73A", fg="black", font="Lato 12", padx="5", pady="5", borderwidth=2, relief="groove")    
        name.grid(row=row,column=1, sticky=N+S+E+W)             

        # Increment row
        row = row + 1 

    # Empty the API
    api_content = ""

    # Botão de Update ( faz um "refresh" nos dados )                    # SEM "()" aqui
    name = Button(tk_inst,text="Update", bg="#1E1E1E", fg="White",command=wallet, font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")   
    name.grid(row=row + 1,column=1, sticky=N+S+E+W)

# Instance to use the module
tk_inst = Tk()

# Call Function
wallet()

# Window Title
tk_inst.title("Crypto GUI")

# Icon ( MUST BE .ICO)
tk_inst.iconbitmap('bitcoin.ico')

# Faz o "Corpo" da tabela a ser usada
name = Label(tk_inst,text="Crypto", bg="#1E1E1E", fg="white", font="Lato 11 bold", padx="5", pady="5", borderwidth=2, relief="groove")      
name.grid(row=0,column=0, sticky=N+S+E+W)                                                                                                                                

name = Label(tk_inst,text="Price Now", bg="#1E1E1E", fg="white", font="Lato 11 bold", padx="5", pady="5", borderwidth=2, relief="groove")    
name.grid(row=0,column=1, sticky=N+S+E+W)               

tk_inst.mainloop()
