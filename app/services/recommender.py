import pandas as pd
import pickle

with open("models/cosine_similarity_model.pkl", "rb") as f:
    similarity_df = pickle.load(f)

interactions_df = pd.read_csv("data/cleaned_interactions.csv")

def get_similar_products(product_id, top_n=5):
    if product_id not in similarity_df.columns:
        return []
    sorted_similar = similarity_df[product_id].sort_values(ascending=False)
    return sorted_similar.iloc[1:top_n+1].index.tolist()

def get_trending_products():
    recent = interactions_df.sort_values(by="timestamp", ascending=False)
    trending = recent['product_id'].value_counts().head(5).index.tolist()
    return trending