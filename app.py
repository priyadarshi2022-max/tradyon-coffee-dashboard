# app.py
import streamlit as st
from ask_me_anything import ask_anything
from coffee_pulse import get_coffee_pulse
from daily_prices import get_global_arabica_price
from daily_prices_extra import get_brazil_coffee_price, get_vietnam_coffee_price

st.set_page_config(page_title="Coffee Ask-Me-Anything", layout="wide")
st.title("☕ Coffee Ask-Me-Anything (Serper + Gemini)")

query = st.text_input("Ask a coffee trade question:")
if st.button("Search"):
    with st.spinner("Fetching real data and summarizing..."):
        try:
            answer = ask_anything(query)
            st.markdown("### ✅ Answer")
            st.write(answer)
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("## ☕ Coffee Pulse — Latest Market News")
if st.button("Fetch Coffee News"):
    with st.spinner("Fetching and summarizing global coffee market news..."):
        news_items = get_coffee_pulse()
        for item in news_items:
            st.markdown(f"**{item['title']}**")
            st.write(item["summary"])
            st.markdown(f"[Read more]({item['url']})")
            st.markdown("---")


st.header("📈 Daily Coffee Prices (Global & Regional)")
if st.button("Fetch Coffee Prices"):
    with st.spinner("Fetching current market data..."):
        results = [
            get_global_arabica_price(),
            get_brazil_coffee_price(),
            get_vietnam_coffee_price()
        ]

        for r in results:
            st.markdown(f"### {r['market']}")
            if "error" in r:
                st.error(f"Error: {r['error']}")
            elif "price_usd" in r:
                st.write(f"Price: ${r['price_usd']}")
                st.write(f"Change: {r['change_usd']} ({r['change_percent']}%)")
            elif "price" in r:
                st.write(f"Approximate Price: {r['price']}")
            st.markdown("---")
