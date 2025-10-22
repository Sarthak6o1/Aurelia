from contextlib import asynccontextmanager
from fastapi import FastAPI
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

load_dotenv()

def load_models_and_clients():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    es_client = Elasticsearch(
        cloud_id=os.getenv("ES_CLOUD_ID"),
        basic_auth=(os.getenv("ES_USER"), os.getenv("ES_PASS"))
    )
    print("Elasticsearch and SentenceTransformer model loaded.")
    return model, es_client

@asynccontextmanager
async def lifespan(app: FastAPI):
    model, es_client = load_models_and_clients()
    app.state.model = model
    app.state.es_client = es_client
    yield
    print("Application shutdown.")
