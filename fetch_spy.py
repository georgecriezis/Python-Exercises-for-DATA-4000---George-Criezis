import yfinance as yf
import pandas as pd


def fetch_spy(period_years=5, outfile="spy_5y_ohlc.csv"):
    # Download daily data for SPY for the last `period_years` years
    df = yf.download("SPY", period=f"{period_years}y", interval="1d", progress=False)
    # Select OHLC columns
    df = df[["Open", "High", "Low", "Close"]].copy()
    df.index.name = "Date"
    df.to_csv(outfile, index=True)
    print(f"Saved {len(df)} rows to {outfile}")
    print(df.tail())
    return df


if __name__ == "__main__":
    fetch_spy()