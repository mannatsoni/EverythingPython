class TradingStrategy:
    def __init__(self,symbol,amount):
        self.symbol = symbol
        self.amount = amount
        self.position = 0
        
    def Buy(self,price,quantity):
        if self.amount >= price*quantity:
            self.position +=quantity
            self.amount -= price*quantity
            print(f"Successfully bought {quantity} shares of {self.symbol} at {price}")
        else:
            print("Not enough amount to proceed with the trade.")
    
    def Sell(self,price,quantity):
        if self.position >= quantity:
            self.position -=quantity
            self.amount += price*quantity
            print(f"Successfully sold {quantity} shares of {self.symbol} at {price}")
        else:
            print("No shares to sell.")

    def Status(self):
        print(f"Current position {self.position} of shares.")
        print(f"Remaining Amount {self.amount}.")
    


momentum = TradingStrategy("BTC", 5000)

print(momentum.symbol)

momentum.Buy(120000000,10)
print(momentum.amount)
print(momentum.position)