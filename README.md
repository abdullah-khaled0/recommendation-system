# 🔥 FastAPI Product Recommendation System

A **FastAPI-based** product recommendation system that uses **TF-IDF** and **Cosine Similarity** to suggest similar products based on their features.

---

## 📹 Demo
![Demo](demo.gif)
> Check out the application in action!

---


## 🚀 Features
- FastAPI backend for real-time product recommendations
- Uses **TF-IDF Vectorization** for feature extraction
- Computes **Cosine Similarity** for recommendations
- Accepts JSON input via **POST API**
- Deployed on **Railway** 🚀
- Integrated with **Flutter app** 📱

## 📦 Installation

1️⃣ **Clone the repository:**
```sh
git clone https://github.com/abdullah0150/recommendation-system.git
cd recommendation-system
```

2️⃣ **Create a virtual environment (optional but recommended):**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3️⃣ **Install dependencies:**
```sh
pip install -r requirements.txt
```

## 🏃‍♂️ Running the Application

1️⃣ **Start the FastAPI server:**
```sh
uvicorn recommender:app --reload
```

2️⃣ **Test the API using Postman or CURL:**

- **POST Request:** 
- **Request Body (JSON):**
```json
{
  "product_name": "Samsung",
  "num_recommendations": 5
}
```
- **Response Example:**
```json
{
  "recommendations": [
    "Samsung Galaxy S21",
    "Samsung Galaxy S20",
    "Samsung Galaxy Note 10",
    "Samsung Galaxy A52",
    "Samsung Galaxy Z Flip"
  ]
}
```

## 📲 Flutter Integration
- The API is fully integrated with a **Flutter application**.


## 🛠 Deployment on Railway
- The API is deployed on **Railway** for easy scalability and hosting.
- To deploy on Railway:
  1. Push your project to GitHub.
  2. Link the GitHub repo to **Railway**.
  3. Set environment variables if needed.
  4. Deploy and get your API URL!



## 🤝 Contributing
Feel free to contribute! Fork and improve the system.
