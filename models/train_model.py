import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle

def train_similarity_model(input_path="data/cleaned_interactions.csv"):
    df = pd.read_csv(input_path)
    user_product_matrix = df.pivot_table(index='user_id', columns='product_id', aggfunc='size', fill_value=0)
    similarity = cosine_similarity(user_product_matrix.T)
    similarity_df = pd.DataFrame(similarity, index=user_product_matrix.columns, columns=user_product_matrix.columns)
    
    with open("models/cosine_similarity_model.pkl", "wb") as f:
        pickle.dump(similarity_df, f)

if __name__ == "__main__":
    train_similarity_model()