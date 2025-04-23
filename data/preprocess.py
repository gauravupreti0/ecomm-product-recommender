import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_interactions(path="data/interactions.csv"):
    df = pd.read_csv(path)
    df.dropna(subset=["user_id", "product_id"], inplace=True)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

if __name__ == "__main__":
    df = preprocess_interactions()
    df.to_csv("data/cleaned_interactions.csv", index=False)