# daily_prices_extra.py
import requests
from bs4 import BeautifulSoup

def get_brazil_coffee_price():
    """
    Scrape retail coffee price in Brazil (Selina Wamucii)
    """
    url = "https://www.selinawamucii.com/insights/prices/brazil/coffee/"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        text = soup.get_text()
        if "The retail price range in Brazilian Real for coffee is between" in text:
            snippet = text.split("The retail price range in Brazilian Real for coffee is between")[1]
            price_line = snippet.split("in Brasilia")[0].strip()
            return {"market": "Brazil Retail Coffee", "price": price_line}
        else:
            return {"market": "Brazil Retail Coffee", "error": "Price text not found"}
    except Exception as e:
        return {"market": "Brazil Retail Coffee", "error": str(e)}

def get_vietnam_coffee_price():
    """
    Scrape retail coffee price in Vietnam (Selina Wamucii)
    """
    url = "https://www.selinawamucii.com/insights/prices/vietnam/coffee/"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        text = soup.get_text()
        if "The retail price range in Vietnamese Dong for coffee is between" in text:
            snippet = text.split("The retail price range in Vietnamese Dong for coffee is between")[1]
            price_line = snippet.split("in Hanoi")[0].strip()
            return {"market": "Vietnam Retail Coffee", "price": price_line}
        else:
            return {"market": "Vietnam Retail Coffee", "error": "Price text not found"}
    except Exception as e:
        return {"market": "Vietnam Retail Coffee", "error": str(e)}
