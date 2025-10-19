# daily_prices.py
import yfinance as yf

def get_global_arabica_price():
    """
    Fetch Arabica Coffee futures price (USD/lb) from Yahoo Finance (ticker KC=F).
    """
    try:
        ticker = yf.Ticker("KC=F")  # ICE Coffee C Futures
        data = ticker.history(period="5d")  # last 5 days
        latest = data.tail(1)
        price = float(latest["Close"].values[0])
        prev = float(data["Close"].iloc[-2])
        change = round(price - prev, 2)
        pct_change = round((change / prev) * 100, 2)
        return {
            "market": "Arabica Coffee Futures (ICE via Yahoo Finance)",
            "price_usd": price,
            "change_usd": change,
            "change_percent": pct_change
        }
    except Exception as e:
        return {"market": "Arabica Coffee Futures", "error": str(e)}
