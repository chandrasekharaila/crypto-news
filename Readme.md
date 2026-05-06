# Crypto Event Intelligence

- FastAPI
- Streamlit
- RSS Aggregation
- Event Classification
- Importance Scoring

The system fetches crypto news from multiple sources, classifies market events, scores their importance, and visualizes them in a real-time intelligence dashboard.

---

# Features

- Multi-source RSS aggregation
- Event classification
- Importance scoring engine
- High / Medium / Low signal categorization
- Streamlit dashboard
- Search & filtering
- Auto refresh
- Real-time market intelligence feed

---

# Tech Stack

- Python
- FastAPI
- Streamlit
- Pandas
- Feedparser

---

# Project Structure

```bash
crypto-news/
│
├── app/
│   ├── api/
│   ├── fetchers/
│   ├── pipelines/
│   ├── processors/
│   ├── utils/
│   └── main.py
│
├── dashboard/
│   └── dashboard.py
│
├── output/
│   └── crypto_news.json
│
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/chandrasekharaila/crypto-event-intelligence.git

cd crypto-event-intelligence
```

---

# Create Virtual Environment

## Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

## Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Backend API

```bash
uvicorn app.main:app --reload
```

API runs on:

```text
http://127.0.0.1:8000
```

---

# Run Streamlit Dashboard

```bash
streamlit run dashboard/dashboard.py
```

Dashboard runs on:

```text
http://localhost:8501
```

---

# API Routes

## Important News

```text
GET /important-news
```

Returns processed crypto event intelligence feed.

---

# Sources

- CoinDesk
- Cointelegraph
- Decrypt
- The Block
- CryptoSlate

---

# Future Improvements

- AI summarization
- Vector search
- Live websocket feeds
- Telegram alerts
- LLM-based event analysis
- Entity relationship graphs
- Historical analytics
- Sentiment analysis

---

# License

MIT
