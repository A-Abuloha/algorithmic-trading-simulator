from data_engine import MarketDataEngine
from portfolio import PortfolioTracker
from strategy import TradingStrategy
import matplotlib.pyplot as plt

E = MarketDataEngine(r"Data/vix-daily.csv")
E.load_data()
P = PortfolioTracker()
S = TradingStrategy()

dates_history = []
portfolio_history = []

for day in range(2, E.get_data_length()):
    current_price = E.get_market_info(day)
    current_date = E.data.loc[day, "DATE"]

    Evaluation = S.evaluate(day, E.data)

    if Evaluation == "BUY":
        shares_to_buy = int(P.cash // current_price)
        if shares_to_buy > 0:
            P.buy(shares_to_buy, current_price, current_date)
    
    elif Evaluation == "SELL":
        if P.shares > 0:
            P.sell(P.shares, current_price, current_date)

    dates_history.append(current_date)
    portfolio_history.append(P.get_total_value(current_price))
final_price = E.get_market_info(E.get_data_length() -1)
final_value = P.get_total_value(final_price)

print("--- Simulation Completed ---")
print(f"Final Cash Balance: ${P.cash:.2f}") 
print(f"Total Portfolio Value: ${final_value:.2f}")
print(f"\n--- TRANSACTION LOG ---")
for trade in P.trade_log:
    print(trade)
               
plt.figure(figsize = (12,6))
plt.plot(dates_history, portfolio_history, label="Algorathmic Strategy", color = "green")
plt.title("Portfolio Growth Over Time")
plt.xlabel("Date")
plt.ylabel("Portfolio Value ($)")
plt.grid(True, linestyle="--", alpha = 0.5)
plt.legend()
plt.show()