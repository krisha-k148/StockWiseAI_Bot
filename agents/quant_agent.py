import yfinance as yf
import pandas as pd

class QuantAgent:
    def __init__(self):
        pass

    def get_recommendation(self, ticker_symbol):
        data = yf.Ticker(ticker_symbol).history(period="3mo")
        if data.empty:
            return {"symbol": ticker_symbol, "decision": "NO DATA"}

        data["SMA_10"] = data["Close"].rolling(window=10).mean()
        data["SMA_30"] = data["Close"].rolling(window=30).mean()

        latest = data.iloc[-1]
        if latest["SMA_10"] > latest["SMA_30"]:
            decision = "BUY"
        elif latest["SMA_10"] < latest["SMA_30"]:
            decision = "SELL"
        else:
            decision = "HOLD"

        return {
            "symbol": ticker_symbol,
            "decision": decision,
            "price": round(latest["Close"], 2),
            "SMA_10": round(latest["SMA_10"], 2),
            "SMA_30": round(latest["SMA_30"], 2),
        }
