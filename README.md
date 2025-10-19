# ☕ Tradyon AI Intern Assignment — *Coffee Intelligence Dashboard*

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/Powered%20by-LangChain-02A095?logo=chainlink)](https://www.langchain.com/)
[![Gemini](https://img.shields.io/badge/LLM-Gemini%202.0%20Flash-4285F4?logo=google)](https://ai.google.dev/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)

---

## 🧭 Overview
The **Coffee Intelligence Dashboard** is an AI-powered system that delivers real-time insights on **coffee commodities** worldwide — combining **web-grounded Q&A**, **market news summarization**, and **live price tracking**.

Built as part of the **Tradyon AI Intern Assignment**, this project demonstrates an end-to-end integration of **LangChain**, **Google Gemini**, **Serper API**, and **Streamlit** — all orchestrated under the **uv environment manager**.

---

## 🏗️ System Architecture
```
User Query / Interaction
      ↓
  [Serper API] — Web Search
      ↓
 [Gemini Model] — Summarization
      ↓
     Output → Streamlit UI
      ↓
 [RSS + Gemini] — Coffee News Pulse
      ↓
 [Yahoo Finance + Scraping] — Daily Prices
```

---

## 🔍 Features

| Module | Description |
|--------|--------------|
| 💬 **Ask-Me-Anything** | Real-time coffee trade Q&A grounded in live web data. |
| 📰 **Coffee Pulse** | Short 2–3 line “Inshorts-style” summaries of market news. |
| 📈 **Daily Prices** | Global & regional coffee price tracker with day-to-day change. |

---

<details>
<summary><b>💬 1️⃣ Ask-Me-Anything (Web Search + Summarization)</b></summary>

**Objective:**  
Enable users to ask natural-language questions like  
> *“What’s the current Arabica price in Brazil?”*  
and get concise, data-grounded summaries.

**Approach:**
1. Query → sent to **Serper API** for web search.  
2. Top 5 snippets (title + URL + content) are formatted using a **LangChain PromptTemplate**.  
3. Passed to **Gemini 2.0 Flash** for summarization & citation.  
4. Displayed instantly in Streamlit chat interface.

**Tech Stack:** `LangChain`, `Serper API`, `Gemini-1.5-Flash`
</details>

---

<details>
<summary><b>📰 2️⃣ Coffee Pulse (Market News)</b></summary>

**Objective:**  
Deliver real-time updates on global coffee trends in short summaries.

**Approach:**
- Fetches coffee-related news via **Google News RSS** (`feedparser`).
- Summarizes each story using **Gemini** into 2–3 factual lines.
- Displays *title + short summary + source link*.

**Example Output:**
> ☕ *Arabica futures rose 3% amid drought in Brazil reducing output.*  
> [Source: Bloomberg]

**Tech Stack:** `feedparser`, `langchain-google-genai`, `Gemini`
</details>

---

<details>
<summary><b>📈 3️⃣ Daily Coffee Prices (Global & Regional)</b></summary>

**Objective:**  
Track daily coffee prices from credible international and regional markets.

**Sources Used:**
| Market | Data Source | Method |
|--------|--------------|--------|
| **Global Arabica (ICE Futures)** | Yahoo Finance (`KC=F`) | `yfinance` |
| **Brazil Retail Coffee** | Selina Wamucii | Web scraping (BeautifulSoup) |
| **Vietnam Retail Coffee** | Selina Wamucii | Web scraping (BeautifulSoup) |

**Displayed Data:**  
- Current price (USD/lb)  
- Daily change (+/- %)  
- Retail ranges in BRL/kg and VND/kg

**Tech Stack:** `yfinance`, `beautifulsoup4`, `requests`
</details>

---

## 🧠 Data Sources Summary

| Module | Source | Access | Data Type |
|--------|---------|--------|-----------|
| Ask-Me-Anything | Serper API | REST (JSON) | Top search results & snippets |
| Coffee Pulse | Google News RSS | FeedParser | News articles |
| Daily Prices | Yahoo Finance | yfinance | Futures price data |
|  | Selina Wamucii | Web scraping | Regional retail prices |

---

## 🧪 Mock Data (Used for Testing)
- Used **mock dictionaries** simulating real API outputs when external APIs failed (e.g., Serper rate limits or RSS timeout).
- Ensured consistent JSON structure during offline debugging.

---

## ⚙️ Tech Stack

| Category | Tools / Frameworks |
|-----------|--------------------|
| **Environment** | `uv`, `python-dotenv` |
| **Frontend / UI** | `streamlit` |
| **LLM / Summarization** | `langchain`, `langchain-google-genai`, `Gemini 1.5 Flash` |
| **Data Retrieval** | `serper`, `feedparser`, `requests` |
| **Parsing & Scraping** | `beautifulsoup4` |
| **Market Data** | `yfinance` |
| **System Utilities** | `json`, `os`, `dotenv` |

---

## ⚙️ Setup & Run Instructions

### 1️⃣ Initialize Project
```
uv init tradyon
cd tradyon
source .venv/bin/activate
```

### 2️⃣ Install Dependencies
```
uv sync
```

### 3️⃣ Set Environment Variables
Create a `.env` file:
```
SERPER_API_KEY=your_serper_key_here
GOOGLE_API_KEY=your_gemini_key_here
```

### 4️⃣ Run Application
```
streamlit run app.py
```

---

## 🚀 Future Enhancements
- 🔄 Auto-refresh “Coffee Pulse” every hour (background scheduler).  
- 📊 Add 7-day **Arabica trend chart** from Yahoo Finance historical data.  
- 💾 Implement **Streamlit caching** (`st.cache_data`) for faster response.  
- 🌍 Expand commodity coverage: tea, cocoa, sugar, etc.  
- 🧮 Add confidence scoring for model-generated responses.

---

## 👨‍💻 Author
**Priyadarshi Kumar**  
🎓 4th Year Undergraduate, Department of Metallurgical & Materials Engineering  
📍 IIT Kharagpur  
💡 Exploring Data Science, Computer Vision & Real-Time AI Systems  
📬 *Developed as part of the Tradyon AI Internship Assignment*

---

⭐ *If you find this project useful, consider starring the repository on GitHub!*  
> _“Grounded AI is good AI.”_ ☕
```
