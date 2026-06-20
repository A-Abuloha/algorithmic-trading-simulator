class PortfolioTracker:
    def __init__(self, initial_cash = 10000.0):
        self.cash = initial_cash
        self.shares = 0
        self.trade_log = []
    
    def buy(self, amount, price, date):
        total_cost = amount * price

        if self.cash >= total_cost:
            self.cash -= total_cost
            self.shares += amount
            self.trade_log.append(
                {
                    "Date" : date,
                    "Type" : "BUY",
                    "Price" : price,
                    "Amount" : amount
                }
            )
        else:
            print("WARNING! Cannot excute!")

    def sell(self, amount, price, date):
        if self.shares >= amount:
            total_earning = amount * price
            self.cash += total_earning
            self.shares -= amount
            self.trade_log.append(
                {
                    "Date" : date,
                    "Type" : "SELL",
                    "Price" : price,
                    "Amount" : amount
                }
            )
        else:
            print("WARNING! Cannot excute!")
    
    def get_total_value(self, current_price):
        return self.cash + (self.shares * current_price)
    