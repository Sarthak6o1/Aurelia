# ⚡ Aurelia - Product Search Engine

**Aurelia** is an AI-driven product discovery engine that integrates **Elasticsearch**, **Google Gemini**, and the **YouTube Data API** to deliver intelligent, semantic search and contextual recommendations. The platform enables fast, meaningful product discovery with dynamic video insights — powered by advanced AI models and scalable backend infrastructure.

---

## 🧩 Tech Stack

**Backend:** FastAPI · Elasticsearch · SentenceTransformers · Google Gemini  
**Frontend:** React.js · Node.js  
**AI/NLP:** Google Vertex AI (Gemini) · Sentence Transformers  
**Cloud Services:** YouTube Data API · Google Cloud Console  
**Tools:** Python · pip · npm · dotenv  

---

## 🧠 Project Overview

Aurelia intelligently processes user queries through multiple AI-driven layers:
1. Performs **semantic and keyword-based search** using Elasticsearch  
2. Leverages **Google Gemini** for item extraction and summarization  
3. Fetches **contextually relevant YouTube videos** using the Data API  
4. Displays products and videos through an intuitive **React.js** interface  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Sarthak6o1/Aurelia.git
cd Aurelia
```

---

### 2️⃣ Backend Setup (FastAPI + AI Integration)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

#### Create a `.env` file in `/backend/` directory:
```bash
# Google Gemini API Key
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
```

#### Run the backend server:
```bash
python run.py
```
Backend runs on `http://localhost:8000`

---

### 3️⃣ Frontend Setup (React.js)
```bash
cd frontend
npm install
npm run start
```
Frontend runs on `http://localhost:3000`

---

## 🌐 API Endpoints

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/api/search` | GET | Performs product search and fetches related videos |

Example:
```
http://localhost:8000/api/search?q=smartphone
```

---

## 🧠 How It Works

1. User inputs a query → e.g., “wireless headphones”  
2. **Elasticsearch** retrieves relevant catalog items via hybrid (semantic + keyword) search  
3. **Gemini model** refines search results by identifying precise product names  
4. **YouTube API** surfaces contextual product videos  
5. The frontend seamlessly displays both products and video results  

---

## 🧾 Skills & Technologies

**AI / ML:** NLP · Semantic Search · Text Embeddings · Content Summarization  
**Cloud / APIs:** Google Gemini API · Vertex AI · YouTube Data API · Elasticsearch Cloud  
**Backend:** FastAPI · Python · SentenceTransformers  
**Frontend:** React.js · Node.js  
**Utilities:** REST APIs · dotenv · JSON Handling · API Integration  

---

## 📁 Project Structure

```
AURELIA/
├── backend/
│   ├── app/
│   │   ├── api.py
│   │   ├── core.py
│   │   ├── main.py
│   │   ├── search_service.py
│   │   └── __init__.py
│   ├── .env
│   ├── requirements.txt
│   └── run.py
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── ProductList.js
│   │   │   └── VideoList.js
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   ├── package.json
│   └── package-lock.json
│
└── README.md
```

---

## 👥 Authors

**Sarthak**  
GitHub: [https://github.com/Sarthak6o1](https://github.com/Sarthak6o1)

**Shashwat Gupta**  
GitHub: [https://github.com/shashwatguptaa](https://github.com/shashwatguptaa)

---

## 🪪 License

Licensed under the **MIT License**.
