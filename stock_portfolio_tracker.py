import os

stock_prices = {
    "AAPL": 175.50,
    "GOOGL": 2850.25,
    "MSFT": 320.40,
    "TSLA": 750.80,
    "INFY": 1450.00,
    "RELIANCE": 2550.75
}

portfolio = {}

print("Enter your stock holdings (type 'done' to finish):")
while True:
    stock = input("Stock symbol (e.g., AAPL): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in our price list.")
        continue
    try:
        quantity = int(input(f"Quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Invalid quantity. Please enter a number.")

print("\n--- Portfolio Summary ---")
total_investment = 0
portfolio_details = []

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value
    print(f"{stock}: {quantity} × ₹{price:.2f} = ₹{value:.2f}")
    portfolio_details.append((stock, quantity, price, value))

print(f"\nTotal Investment Value: ₹{total_investment:.2f}")

save_option = input("Do you want to save this report? (yes/no): ").strip().lower()

if save_option == 'yes':
    output_format = input("Choose format: txt or csv: ").strip().lower()
    os.makedirs("output", exist_ok=True)
    
    if output_format == 'txt':
        with open("output/portfolio_report.txt", "w") as file:
            file.write("--- Portfolio Report ---\n")
            for stock, qty, price, val in portfolio_details:
                file.write(f"{stock}: {qty} × ₹{price:.2f} = ₹{val:.2f}\n")
            file.write(f"\nTotal Investment: ₹{total_investment:.2f}")
        print("Report saved to output/portfolio_report.txt")
        
    elif output_format == 'csv':
        with open("output/portfolio_report.csv", "w") as file:
            file.write("Stock,Quantity,Price,Value\n")
            for stock, qty, price, val in portfolio_details:
                file.write(f"{stock},{qty},{price:.2f},{val:.2f}\n")
            file.write(f"Total,,,{total_investment:.2f}")
        print("Report saved to output/portfolio_report.csv")
        
    else:
        print("Invalid format. Report not saved.")

