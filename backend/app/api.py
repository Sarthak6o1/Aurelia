from fastapi import APIRouter, Query, Request
from typing import Optional
import os
from google import genai
from . import search_service

router = APIRouter()
client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

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
    model = request.app.state.model
    es_client = request.app.state.es_client

    product_results = search_service.elastic_composite_product_search(
        query=q,
        es_client=es_client,
        model=model,
        min_price=min_price,
        max_price=max_price,
        min_size_value=min_size_value,
        max_size_value=max_size_value,
        size_unit=size_unit,
        size=50,
    )
    
    if not product_results:
        return {"query": q, "products": [], "videos": []}

    top_titles = [hit["_source"].get("product_title", "") for hit in product_results[:15]]
    catalog_texts = [hit["_source"].get("catalog_content", "") for hit in product_results[:15]]

    # Prepare top 10 ES results
    top10_catalogs = product_results[:10]
    youtube_videos = []

    for hit in top10_catalogs:
        catalog_content = hit["_source"].get("catalog_content", "")
        gemini_response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=(
                f"From the following product catalog content, extract the exact item name only, "
                f"no extra text:\n{catalog_content}"
            )
        )
        item_name = gemini_response.text.strip()
        if not item_name:
            item_name = hit["_source"].get("product_title", "")

        # Fetch YouTube videos for this item
        videos = search_service.youtube_search(
            query=item_name,
            max_results=3
        )
        youtube_videos.extend(videos)

    # Deduplicate videos by URL
    seen_urls = set()
    unique_videos = []
    for video in youtube_videos:
        if video["url"] not in seen_urls:
            unique_videos.append(video)
            seen_urls.add(video["url"])

    best_keyword_query = search_service.extract_best_keywords(top_titles, model, catalog_texts)

    return {
        "query": q,
        "products": product_results[:20],
        "videos": unique_videos
    }
