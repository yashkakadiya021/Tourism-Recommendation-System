
# 🧭 Tourism Recommendation System (Flask App)

A web-based tourism recommendation system that suggests **destinations** and **hotels** based on category, location, price, and user preferences using **Flask**, **pandas**, and **scikit-learn**. The interface is built with dynamic HTML and CSS, and the backend logic includes content-based filtering and scoring mechanisms for hotel rankings.

---

## 📌 Features

### 🌍 Destination Recommendation
- Choose from categories like **Historical**, **Beaches**, **Mountains**, **Adventure**, and more.
- Top-rated places recommended using a content-based filter with **TF-IDF + Cosine Similarity**.

### 🏨 Hotel Recommendation
- Get hotel suggestions based on **city** and **maximum price**.
- Hotels are ranked using a **custom score**:
  - 70% rating (normalized)
  - 30% inverse price (cheaper is better)
- Also displays **facilities** and **nearby places**.

---

## 📁 Project Structure

📦 Tourism-Recommendation-System  

├── model_flask.py                         # Main Flask app  
├── final_places.csv                       # Dataset for places  
├── final_hotel.csv                        # Dataset for hotels  
├── static/                                # Static files like background images  
│ ├── 6346166.jpg  
│ ├── bg-destination.jpg  
│ └── bg-hotel.jpg  
└── README.md  

---

## ⚙️ Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Tourism-Recommendation-System.git
cd Tourism-Recommendation-System
```

📊 Core Logic

🔍 Destination Recommender
Combines category and city into a single feature.

Uses TF-IDF Vectorizer to vectorize place descriptions.

Calculates cosine similarity to recommend similar places by category.


🛠️ Technologies Used

Python

Flask

Pandas

Scikit-learn

HTML/CSS (inline in Flask app)

TF-IDF & Cosine Similarity


💡 Future Enhancements

Deploy app on Render, Streamlit, or Heroku

Add user login for personalization

Save user history and preferences

Improve recommendation algorithm with collaborative filtering


🤝 Contributing

Feel free to fork this project and submit a pull request with your improvements!







