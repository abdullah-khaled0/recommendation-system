from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd


app = FastAPI()

# Load the dataset and saved models
df = pd.read_csv("products.csv")
with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
with open("cosine_similarity.pkl", "rb") as f:
    cosine_sim = pickle.load(f)

# Define request model
class RecommendationRequest(BaseModel):
    product_name: str
    num_recommendations: int = 10

# Recommendation function
def recommend_products(product_name: str, num_recommendations: int = 10):
    try:
        product_idx = df[df['Product Name'].str.contains(product_name, case=False)].index[0]
        sim_scores = list(enumerate(cosine_sim[product_idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
        recommendations = [df.iloc[i[0]]['Product Name'] for i in sim_scores]
        return {"recommendations": recommendations}
    except IndexError:
        raise HTTPException(status_code=404, detail="Product not found!")

@app.post("/recommend/")
def get_recommendations(request: RecommendationRequest):
    return recommend_products(request.product_name, request.num_recommendations)