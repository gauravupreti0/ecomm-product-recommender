## E-commerce Product Recommender System

### Overview

A FastAPI-powered recommendation engine suggesting similar and trending products using collaborative filtering.

### Tech Stack

- FastAPI
- Scikit-learn
- Pandas
- MongoDB
- Docker (optional)

### How to Run

```bash
pip install -r requirements.txt
python data/preprocess.py
python models/train_model.py
uvicorn main:app --reload
```
