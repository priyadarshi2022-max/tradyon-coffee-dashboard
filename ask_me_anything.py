# ask_me_anything.py
import os
import requests
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ---------- STEP 1: Web Search using Serper ----------
def get_serper_results(query: str, num_results: int = 5):
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    res = requests.post(url, headers=headers, data=payload)
    res.raise_for_status()
    data = res.json()
    organic_results = data.get("organic", [])[:num_results]

    formatted_sources = [
        f"[Source {i}: {r['link']}]\nContent: {r['snippet']}\n"
        for i, r in enumerate(organic_results, 1)
    ]
    return "\n".join(formatted_sources)

# ---------- STEP 2: Summarize using Gemini ----------
def summarize_with_gemini(question: str, web_context: str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.2,
        google_api_key=GOOGLE_API_KEY
    )

    prompt = f"""
You are an expert coffee commodity analyst.
Use only the factual information from the search results below to answer the user's question.
Summarize concisely and cite sources if available.

Question: {question}

Web Search Results:
{web_context}
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

# ---------- STEP 3: Combined function ----------
def ask_anything(question: str):
    context = get_serper_results(question)
    answer = summarize_with_gemini(question, context)
    return answer
