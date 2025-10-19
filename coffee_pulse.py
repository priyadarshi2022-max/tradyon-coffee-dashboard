# coffee_pulse.py
import feedparser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def fetch_coffee_news_rss(max_items=5):
    """
    Fetch latest coffee market news from Google News RSS.
    Returns list of dicts [{title, link, summary}]
    """
    FEED_URL = "https://news.google.com/rss/search?q=coffee+commodity+OR+coffee+market+OR+arabica+coffee&hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(FEED_URL)

    articles = []
    for entry in feed.entries[:max_items]:
        title = entry.get("title", "")
        link = entry.get("link", "")
        desc = entry.get("summary", "")
        articles.append({"title": title, "url": link, "content": desc})
    return articles

def summarize_articles(articles):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.3,
        google_api_key=GOOGLE_API_KEY
    )

    summaries = []
    for art in articles:
        prompt = f"""
Summarize this coffee market news in 2–3 short, factual lines ('Inshorts'-style).

Title: {art['title']}
Content: {art['content']}
"""
        try:
            response = llm.invoke([HumanMessage(content=prompt)])
            summaries.append({
                "title": art["title"],
                "summary": response.content.strip(),
                "url": art["url"]
            })
        except Exception as e:
            summaries.append({
                "title": art["title"],
                "summary": f"Error: {e}",
                "url": art["url"]
            })
    return summaries

def get_coffee_pulse():
    news = fetch_coffee_news_rss()
    return summarize_articles(news)
