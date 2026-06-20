import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("stock_prices_practice_dataset.csv")

while True:
    print("\nSTOCK MARKET ANALYZER")
    print("1. Analyze one stock")
    print("2. Analyze Two stocks")
    print("3. Best Performing Stock")
    print("4. Highest Average Volume")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if not choice.isdigit():
        print("Enter a number from 1 to 5.")
        continue

    choice = int(choice)
    if choice == 1:
        ticker = input("Enter stock ticker: ")
        stock = df[df["Ticker"] == ticker]

        if stock.empty:
            print("Ticker not found.")
        else:
            starting = stock.iloc[0]["Open"]
            ending = stock.iloc[-1]["Close"]
            return_percent = (ending - starting) / starting * 100
            highest = stock["High"].max()
            lowest = stock["Low"].min()
            average_volume = stock["Volume"].mean()
            print(f"\nTicker: {ticker}")
            print(f"Starting Price: ${starting:.2f}")
            print(f"Ending Price: ${ending:.2f}")
            print(f"Return: {return_percent:.2f}%")
            print(f"Highest Price: ${highest:.2f}")
            print(f"Lowest Price: ${lowest:.2f}")
            print(f"Average Volume: {average_volume:,.0f}")

            plt.plot(stock["Date"], stock["Close"])
            plt.title(f"{ticker} Stock Price")
            plt.xlabel("Date")
            plt.ylabel("Close Price")
            plt.show()
    elif choice == 2:
        ticker1 = input("First ticker: ").upper()
        ticker2 = input("Second ticker: ").upper()

        stock1 = df[df["Ticker"] == ticker1]
        stock2 = df[df["Ticker"] == ticker2]

        if stock1.empty or stock2.empty:
            print("One or both tickers were not found.")
        else:
            start1 = stock1.iloc[0]["Open"]
            end1 = stock1.iloc[-1]["Close"]
            return1 = (end1 - start1) / start1 * 100

            start2 = stock2.iloc[0]["Open"]
            end2 = stock2.iloc[-1]["Close"]
            return2 = (end2 - start2) / start2 * 100

            print(f"{ticker1} Return: {return1:.2f}%")
            print(f"{ticker2} Return: {return2:.2f}%")

            if return1 > return2:
                print(f"{ticker1} performed better.")
            elif return2 > return1:
                print(f"{ticker2} performed better.")
            else:
                print("Both stocks had the same return.")
            plt.plot(stock1["Date"], stock1["Close"], label=ticker1)
            plt.plot(stock2["Date"], stock2["Close"], label=ticker2)

            plt.title(f"{ticker1} vs {ticker2} Closing Prices")
            plt.xlabel("Date")
            plt.ylabel("Close Price")
            plt.xticks(rotation=45)
            plt.legend()
            plt.tight_layout()
            plt.show()
    elif choice == 3:
        returns = []
        for ticker in df["Ticker"].unique():
            stock = df[df["Ticker"] == ticker]

            start = stock.iloc[0]["Open"]
            end = stock.iloc[-1]["Close"]

            return_percent = (end - start) / start * 100
            returns.append([ticker, return_percent])

        returns_df = pd.DataFrame(returns, columns=["Ticker", "Return"])
        best = returns_df.sort_values("Return", ascending=False)

        print("\nSTOCK RETURNS")
        print(best.to_string(index=False))
    elif choice == 4:
        volume_data = []

        for ticker in df["Ticker"].unique():
            stock = df[df["Ticker"] == ticker]

            avg_volume = stock["Volume"].mean()
            volume_data.append([ticker, avg_volume])

            volume_df = pd.DataFrame(volume_data, columns=["Ticker", "Volume"])
            best2 = volume_df.sort_values("Volume", ascending=False)

        print("\nHIGHEST AVERAGE VOLUMES")
        print(best2.to_string(index=False))
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
