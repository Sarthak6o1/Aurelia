from fastapi import APIRouter, Query, Request
from typing import Optional

from . import search_service # Import the updated service

router = APIRouter()

@router.get("/search")
async def advanced_search_api(
    request: Request,
    q: str = Query(..., min_length=1),
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    min_size_value: Optional[float] = None,
    max_size_value: Optional[float] = None,
    size_unit: Optional[str] = None,
):
    # Get model and client from app state (loaded during lifespan)
    model = request.app.state.model
    es_client = request.app.state.es_client

    # Fetch results using the script_score method
    product_results = search_service.elastic_composite_product_search(
        query=q,
        es_client=es_client,
        model=model, # Pass the loaded model
        min_price=min_price,
        max_price=max_price,
        min_size_value=min_size_value,
        max_size_value=max_size_value,
        size_unit=size_unit,
        size=50, # Fetch 50 for keyword context
    )
    
    if not product_results:
        return { "query": q, "products": [], "videos": [] }

    # Extract keywords locally
    top_titles = [hit["_source"].get("product_title", "") for hit in product_results[:15]]
    catalog_texts = [hit["_source"].get("catalog_content", "") for hit in product_results[:15]]
    best_keyword_query = search_service.extract_best_keywords(top_titles, model, catalog_texts)
    youtube_query = best_keyword_query or q 
    
    # Search YouTube
    video_results = search_service.youtube_search(
        query=youtube_query,
        max_results=8
    )
    
    # Return top 20 products
    return {
        "query": q,
        "products": product_results[:20], 
        "videos": video_results
    }