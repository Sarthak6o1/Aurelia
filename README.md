# ⚡ Aurelia - AI-Driven Product Search Engine

**Aurelia** is an AI-driven product discovery engine that integrates **Elasticsearch**, **Google Gemini**, and the **YouTube Data API** to deliver intelligent, semantic search and contextual recommendations. The platform enables fast, meaningful product discovery with dynamic video insights and an interactive **AI Assistant** — all powered by advanced AI models and scalable backend infrastructure.

---

## 🧩 Tech Stack

**Backend:** FastAPI · Elasticsearch · SentenceTransformers · **Google Gemini**  
**Frontend:** React.js · Node.js  
**AI/NLP:** Google Vertex AI (Gemini) · Sentence Transformers  
**Cloud Services:** YouTube Data API · Google Cloud Console  
**Tools:** Python · pip · npm · dotenv  

---

## 🧠 Project Overview

Aurelia intelligently processes user queries through multiple AI-driven layers, providing both search results and instant assistance:
1. Performs **semantic and keyword-based search** using Elasticsearch.  
2. Leverages **Google Gemini** for item extraction, summarization, and powering the **AI Chatbot**.  
3. Fetches **contextually relevant YouTube videos** using the Data API.  
4. Provides **instant, conversational help** via the integrated chatbot.  
5. Displays products and videos through an intuitive **React.js** interface.  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone [https://github.com/Sarthak6o1/Aurelia.git](https://github.com/Sarthak6o1/Aurelia.git)
cd Aurelia
2️⃣ Backend Setup (FastAPI + AI Integration)Bashcd backend
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate    # Windows
pip install -r requirements.txt
Create a .env file in /backend/ directory:Bash# Google Gemini API Key
GENAI_API_KEY="your_gemini_api_key_here"

# Elasticsearch Configuration
ES_CLOUD_ID="your_elasticsearch_cloud_id_here"
ES_USER="your_elasticsearch_username_here"
ES_PASS="your_elasticsearch_password_here"
ES_INDEX_NAME="your_index_name_here"

# YouTube API Key
YOUTUBE_API_KEY="your_youtube_api_key_here"

# Vertex AI Configuration
PROJECT_ID="your_vertex_project_id_here"
LOCATION="us-central1"
MODEL_ID="gemini-2.0-flash-001"
Run the backend server:Bashpython run.py
Backend runs on http://localhost:80003️⃣ Frontend Setup (React.js)Bashcd frontend
npm install
npm run start
Frontend runs on http://localhost:3000🌐 API EndpointsEndpointMethodDescription/api/searchGETPerforms product search and fetches related videos/api/chatbotPOSTHandles conversational queries for the AI AssistantExample Search:http://localhost:8000/api/search?q=wireless headphones
🧠 How It WorksUser interacts with the UI (query or chat).Search Logic:User inputs a search query.Elasticsearch retrieves relevant catalog items via hybrid (semantic + keyword) search.Gemini model refines search results by identifying precise product names and provides summarization.YouTube API surfaces contextual product videos.Chatbot Logic:User sends a message to the AI Assistant.The request hits the new /api/chatbot endpoint.Gemini model processes the conversational query, providing app guidance or general assistance.The frontend seamlessly displays search results and manages the interactive chatbot UI.🧾 Skills & TechnologiesAI / ML: NLP · Semantic Search · Text Embeddings · Content Summarization · Conversational AI  Cloud / APIs: Google Gemini API · Vertex AI · YouTube Data API · Elasticsearch Cloud  Backend: FastAPI · Python · SentenceTransformers  Frontend: React.js · Modern UI/UX · Node.js  Utilities: REST APIs · dotenv · JSON Handling · API Integration  📁 Project StructureAURELIA/
├── backend/
│   ├── app/
│   │   ├── api.py
│   │   ├── core.py
│   │   ├── main.py
│   │   ├── search_service.py
│   │   ├── bot_api.py  <-- NEW: Handles Chatbot requests
│   │   └── __init__.py
│   ├── .env
│   ├── requirements.txt
│   └── run.py
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── ProductList.js
│   │   │   ├── VideoList.js
│   │   │   └── UserGuideChatbot.js  <-- NEW: Chatbot UI Component
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   ├── package.json
│   └── package-lock.json
│
└── README.md
👥 AuthorsSarthak  GitHub: https://github.com/Sarthak6o1Shashwat Gupta  GitHub: https://github.com/shashwatguptaa🪪 LicenseLicensed under the MIT License.
