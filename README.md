// =============================
// README (setup)
// =============================
// 1) Backend
//    cd backend
//    cp .env.example .env  # set GOOGLE_API_KEY
//    pip install -e .      # or: pip install -r requirements from pyproject
//    uvicorn app.main:app --reload
// 2) Frontend
//    cd frontend
//    npm i
//    npm run dev
// 3) Optional: ingest shop policies or FAQs
//    curl -X POST http://localhost:8000/api/ingest -H 'Content-Type: application/json' \
//      -d '[{"id":"faq1","text":"Delivery within 5km. Cash or card."}]'
// 4) Open http://localhost:5173

// Notes
// - Clean architecture: routers → graph → llm/vector → config/schemas. Loose coupling via DI getters.
// - LangSmith tracing on if LANGSMITH_API_KEY set.
// - Gemini-compatible via langchain-google-genai ChatGoogleGenerativeAI.
// - Pydantic structured output ensures consistent contract for UI.
// - Swap Chroma for another vector DB if needed without touching routers or UI.
