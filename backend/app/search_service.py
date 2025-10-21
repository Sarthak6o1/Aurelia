import requests
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import os
from collections import Counter
import numpy as np
import re
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
INDEX_NAME = os.getenv("INDEX_NAME", "learning_index")

def generate_text_embedding(text: str, model: SentenceTransformer) -> list:
    if not isinstance(text, str):
        text = str(text)
    return model.encode(text).tolist()

def elastic_composite_product_search(
    query: str,
    es_client: Elasticsearch,
    model: SentenceTransformer,
    min_price: float = None,
    max_price: float = None,
    min_size_value: float = None,
    max_size_value: float = None,
    size_unit: str = None,
    size: int = 50, # Keep fetching 50 for keyword context
) -> list:
    
    vector = generate_text_embedding(query, model)
    filters = []

    if min_price is not None or max_price is not None:
        price_range = {}
        if min_price is not None:
            price_range["gte"] = min_price
        if max_price is not None:
            price_range["lte"] = max_price
        filters.append({"range": {"price": price_range}})

    if min_size_value is not None or max_size_value is not None:
        size_range = {}
        if min_size_value is not None:
            size_range["gte"] = float(min_size_value)
        if max_size_value is not None:
            size_range["lte"] = float(max_size_value)
        filters.append({"range": {"size_value": size_range}})

    if size_unit and size_unit in ["ounce", "pcs"]:
        filters.append({"term": {"size_unit": size_unit.lower()}})

    # Body using script_score as per your provided code
    body = {
        "size": size,
        "query": {
            "bool": {
                "filter": filters, # Apply filters without affecting score initially
                "should": [
                    {
                        "multi_match": {
                            "query": query,
                            "fields": [
                                "catalog_content^3",
                                "product_title^2",
                                "brand",
                                "category",
                                "tags",
                            ],
                            "fuzziness": "AUTO",
                        }
                    },
                    {
                        "script_score": {
                            "query": {"match_all": {}}, # Apply to all filtered docs
                            "script": {
                                "source": """
                                    if (doc['content_embedding'].size() == 0) return 0.0;
                                    double cosine = cosineSimilarity(params.query_vector, 'content_embedding');
                                    double dot = dotProduct(params.query_vector, 'content_embedding');
                                    return (cosine > 0 ? cosine : 0) * 0.6 + (dot > 0 ? dot : 0) * 0.3 + 0.1;
                                """,
                                "params": {"query_vector": vector},
                            },
                        }
                    },
                ],
                "minimum_should_match": 1,
            }
        },
    }

    try:
        res = es_client.search(index=INDEX_NAME, body=body)
        return res["hits"]["hits"]
    except Exception as e:
        print(f"--- Elasticsearch Search Error ---")
        print(f"Query Body: {body}")
        print(f"Error: {e}")
        print(f"----------------------------------")
        return []


def extract_best_keywords(products: list, model: SentenceTransformer, catalog_texts: list) -> str:
    valid_products = [p for p in products if p]
    if not valid_products: return ""
    all_titles = " ".join(valid_products)
    all_titles = re.sub(r"[^A-Za-z0-9\s]", " ", all_titles)
    tokens = [w.lower() for w in all_titles.split() if len(w) > 2]
    freq = Counter(tokens)
    if not tokens: return ""

    valid_catalog_texts = [cat for cat in catalog_texts if isinstance(cat, str) and cat.strip()]
    if not valid_catalog_texts: return " ".join(dict(freq.most_common(3)).keys())

    token_embeddings = {t: model.encode(t) for t in freq.keys()}
    catalog_embeddings = [model.encode(cat) for cat in valid_catalog_texts]

    keyword_scores = {}
    for token, emb in token_embeddings.items():
        sims = []
        for cat_emb in catalog_embeddings:
            norm_emb = np.linalg.norm(emb)
            norm_cat_emb = np.linalg.norm(cat_emb)
            cosine = 0.0 if norm_emb == 0 or norm_cat_emb == 0 else np.dot(emb, cat_emb) / (norm_emb * norm_cat_emb)
            cosine = np.clip(cosine, -1.0, 1.0)
            sims.append(cosine)
        avg_sim = np.mean(sims) if sims else 0.0
        score = avg_sim * (1 + np.log1p(freq[token]))
        keyword_scores[token] = score

    sorted_keywords = sorted(keyword_scores.items(), key=lambda item: item[1], reverse=True)
    top_keywords = [kw for kw, score in sorted_keywords[:3]]
    return " ".join(top_keywords)


def youtube_search(query: str, max_results: int = 8) -> list:
    if not YOUTUBE_API_KEY:
        print("--- YouTube API Error ---")
        print("Error: YOUTUBE_API_KEY is not set in .env file.")
        print("---------------------------")
        return []
        
    print(f"Searching YouTube with query: '{query}'")
    endpoint = "https://www.googleapis.com/youtube/v3/search"
    params = { "part": "snippet", "q": query, "type": "video", "maxResults": max_results, "key": YOUTUBE_API_KEY, "safeSearch": "strict" }
    
    try:
        resp = requests.get(endpoint, params=params)
        resp.raise_for_status()
        videos = []
        for item in resp.json().get("items", []):
            vid_id = item.get("id", {}).get("videoId")
            snippet = item.get("snippet")
            if not vid_id or not snippet: continue
            videos.append({ "title": snippet.get("title", "No Title"), "description": snippet.get("description", ""), "url": f"https://www.youtube.com/watch?v={vid_id}" })
        print(f"Found {len(videos)} YouTube videos.")
        return videos
    except requests.RequestException as e:
        print(f"--- YouTube API Error ---")
        if e.response:
            try:
                error_data = e.response.json()
                print(f"Status Code: {e.response.status_code}")
                print(f"Message: {error_data.get('error', {}).get('message', 'No message')}")
            except requests.JSONDecodeError: print(f"Non-JSON error: {e.response.text}")
        else: print(f"Network error: {e}")
        print(f"---------------------------")
        return []