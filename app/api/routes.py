from fastapi import APIRouter
from app.services.recommender import get_similar_products, get_trending_products

router = APIRouter()

@router.get("/recommend/similar")
def similar_products(product_id: str, top_n: int = 5):
    return {"similar_products": get_similar_products(product_id, top_n)}

@router.get("/recommend/trending")
def trending_products():
    return {"trending_products": get_trending_products()}