# Aurelia

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Aurelia is an AI-powered product search and assistant platform that integrates **FastAPI**, **Google Gemini API**, **Vertex AI**, **Elasticsearch**, and **YouTube Data API** with a **React.js frontend** for seamless interactive experiences.

---

## Table of Contents

* [Features](#features)
* [Tech Stack](#tech-stack)
* [Project Structure](#project-structure)
* [Backend Setup](#backend-setup)
* [Frontend Setup](#frontend-setup)
* [API Endpoints](#api-endpoints)
* [How It Works](#how-it-works)
* [Authors](#authors)
* [License](#license)

---

## Features

* **AI / ML:** Semantic Search, NLP, Text Embeddings, Content Summarization, Conversational AI
* **Cloud / APIs:** Google Gemini API, Vertex AI, YouTube Data API, Elasticsearch Cloud
* **Backend:** FastAPI, Python, SentenceTransformers
* **Frontend:** React.js, Modern UI/UX, Node.js
* **Utilities:** REST APIs, dotenv, JSON handling, API integration

---

## Tech Stack

| Layer      | Technology / Service                                  |
| ---------- | ----------------------------------------------------- |
| Backend    | FastAPI, Python, SentenceTransformers                 |
| AI / ML    | Google Gemini API, Vertex AI, NLP                     |
| Search     | Elasticsearch Cloud, Hybrid Semantic + Keyword Search |
| Frontend   | React.js, Node.js, Modern UI Components               |
| Video Data | YouTube Data API                                      |

---

## Project Structure

```
AURELIA/
├── backend/
│   ├── app/
│   │   ├── api.py
│   │   ├── core.py
│   │   ├── main.py
│   │   ├── search_service.py
│   │   ├── bot_api.py            # Chatbot endpoint
│   │   └── __init__.py
│   ├── .env
│   ├── requirements.txt
│   └── run.py
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── ProductList.js
│   │   │   ├── VideoList.js
│   │   │   └── UserGuideChatbot.js  # Chatbot UI
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   ├── package.json
│   └── package-lock.json
└── README.md
```

---

## Backend Setup (FastAPI + AI Integration)

```bash
git clone https://github.com/Sarthak6o1/Aurelia.git
cd Aurelia/backend
python -m venv venv

# Activate virtual environment
# Mac/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in `/backend/`:

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

### Run Backend Server

```bash
python run.py
```

Backend runs at: `http://localhost:8000`

---

## Frontend Setup (React.js)

```bash
cd frontend
npm install
npm run start
```

Frontend runs at: `http://localhost:3000`

---

## API Endpoints

| Endpoint       | Method | Description                                        |
| -------------- | ------ | -------------------------------------------------- |
| `/api/search`  | GET    | Perform product search and fetch related videos    |
| `/api/chatbot` | POST   | Handle conversational queries for the AI assistant |

**Example Search:**
`http://localhost:8000/api/search?q=wireless headphones`

---

## How It Works

### Search Logic

1. User inputs a search query in the frontend.
2. Elasticsearch retrieves relevant catalog items using **hybrid semantic + keyword search**.
3. Gemini model refines results and provides summaries.
4. YouTube API fetches contextual product videos.

### Chatbot Logic

1. User sends a message to the AI assistant.
2. The request hits the `/api/chatbot` endpoint.
3. Gemini processes the query, providing guidance or assistance.
4. Frontend displays search results and chatbot responses seamlessly.

---

## Authors

* **Sarthak** – [GitHub](https://github.com/Sarthak6o1)
* **Shashwat Gupta** – [GitHub](https://github.com/shashwatguptaa)

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
