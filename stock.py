# ask me to pick a stock
#This program asks the user for a stock ticker symbol and a number of years, then fetches and prints the OHLC data for that stock over the specified period.
import yfinance as yf   
import pandas as pd
def fetch_stock_data(ticker="SPY", period_years=5, outfile="stock_ohlc.csv"):
    # Download daily data for the specified ticker for the last `period_years` years
    df = yf.download(ticker, period=f"{period_years}y", interval="1d", progress=False)
    # Select OHLC columns
    df = df[["Open", "High", "Low", "Close"]].copy()
    df.index.name = "Date"
    df.to_csv(outfile, index=True)
    print(f"Saved {len(df)} rows to {outfile}")
    print(df.tail())
    return df

fetch_stock_data()