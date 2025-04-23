from app.db.mongo_client import products_collection

def get_product_by_id(product_id: str):
    return products_collection.find_one({"product_id": product_id})