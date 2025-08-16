# 🍕 PizzaBot

An AI-powered pizza ordering assistant built with **FastAPI**, **LangChain**, **Google Gemini**, and a **Vite + React** frontend.  
PizzaBot supports conversational ordering, policy/FAQ lookup, and flexible vector search.

---

## ⚡ Quickstart

### 1) Backend Setup
```bash
cd backend
cp .env.example .env   # set GOOGLE_API_KEY (and other keys if needed)
pip install -r requirements.txt
uvicorn app.main:app --reload

cd frontend
npm install
npm run dev

curl -X POST http://localhost:8000/api/ingest \
  -H 'Content-Type: application/json' \
  -d '[{"id":"faq1","text":"Delivery within 5km. Cash or card."}]'

📂 Project Structure
pizzabot/
├── backend/          # FastAPI + LangChain services
│   ├── app/          # routers, graph, config, schemas
│   ├── .env.example  # environment template
│   └── requirements.txt
├── frontend/         # Vite + React client
│   ├── src/          # components, pages, API calls
│   └── package.json
└── README.md


🏗️ Architecture

Routers → Graph → LLM / Vector → Config / Schemas

Loose coupling with dependency injection for easier testing & swapping components

Pydantic structured output ensures consistent contracts for UI

Vector DB abstraction: swap Chroma for another database without touching routers or UI

LangSmith tracing auto-enabled if LANGSMITH_API_KEY is set

Gemini-compatible via langchain-google-genai (ChatGoogleGenerativeAI)

🌐 Tech Stack

Backend: FastAPI, LangChain, ChromaDB, Google Gemini

Frontend: React, Vite, Bootstrap

Infra: dotenv, Pydantic, Uvicorn

🔑 Environment Variables

Create .env inside backend/ (see .env.example):

# Google Gemini
GOOGLE_API_KEY=your_api_key_here

# LangSmith (optional)
LANGSMITH_API_KEY=your_langsmith_key_here

# Backend Config
ENV=dev
HOST=0.0.0.0
PORT=8000
VECTORDB_DIR=./data/chroma
FRONTEND_ORIGIN=http://localhost:5173

🚀 Roadmap

 Save orders to database

 User authentication & profiles

 Payment gateway integration

 Multi-LLM backend support (OpenAI, Anthropic, etc.)

 Deployment with Docker

🤝 Contributing

Contributions are welcome!
Fork the repo, create a feature branch, and open a Pull Request.

📜 License

MIT License © 2025 PizzaBot Authors
