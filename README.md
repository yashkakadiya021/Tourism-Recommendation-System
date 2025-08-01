
# 🧭 Tourism Recommendation System (Flask App)

A web-based tourism recommendation system that suggests **destinations** and **hotels** based on category, location, price, and user preferences using **Flask**, **pandas**, and **scikit-learn**. The interface is built with dynamic HTML and CSS, and the backend logic includes content-based filtering and scoring mechanisms for hotel rankings.

---

## 📌 Features

### 🌍 Destination Recommendation
- Choose from categories like **Historical**, **Beaches**, **Mountains**, **Adventure**, and more.
- Top-rated places recommended using a content-based filter with **TF-IDF + Cosine Similarity**.

  <img width="840" height="644" alt="machine learning - visual selection (2)" src="https://github.com/user-attachments/assets/8930b602-22c9-4915-b9a8-169c9cb20d74" />


### 🏨 Hotel Recommendation
- Get hotel suggestions based on **city** and **maximum price**.
- Hotels are ranked using a **custom score**:
  - 70% rating (normalized)
  - 30% inverse price (cheaper is better)
- Also displays **facilities** and **nearby places**.

 <img width="648" height="480" alt="machine learning - visual selection (12)" src="https://github.com/user-attachments/assets/f51e2b4f-2700-4ef9-859e-6853dfaa6244" />



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

### Clone the Repository
```bash
git clone https://github.com/yashkakadiya021/Tourism-Recommendation-System.git
cd Tourism-Recommendation-System
```

## 📊 Data Sources

- 🏞️ **Destinations** scraped from [Holidify](https://www.holidify.com)
- 🏨 **Hotels** scraped from [MakeMyTrip](https://www.makemytrip.com)

---

## 📈 EDA & Model Development

- **EDA**: Visual analysis of destination and hotel datasets
- **Model Logic**:
  - Destination similarity computed using **TF-IDF + Cosine Similarity**
  - Hotel scoring using:
    ```
    Score = 0.7 * normalized_rating + 0.3 * inverse_discounted_price
    ```

- **Evaluation Metrics (for future expansion)**:
  - Precision@K
  - Recall@K
  - NDCG

<img width="624" height="562" alt="machine learning - visual selection (10)" src="https://github.com/user-attachments/assets/1ca2b3f2-e8bd-4210-8d22-8d385fc03fd8" />

---

## 💡 How it Works

- The system recommends destinations by matching **user-selected category** with destination descriptions using **TF-IDF**.
- Hotel recommendations are filtered by **user-selected city** and **maximum price**, then scored based on **ratings and prices**.
- Each result includes key details: Name, Rating, Price, Facilities, and Nearby Attractions.

---

<img width="840" height="778" alt="machine learning - visual selection (8)" src="https://github.com/user-attachments/assets/ec45acd9-1164-43a8-8df1-a90da2f3579a" />


## 🎯 What Users Can Expect

- 🗺️ Top 10 destination suggestions from the chosen category.
- 🏨 Top 10 hotel options that fit within the user’s budget in a specific city.
- 💬 Clear display of essential details for decision-making:
  - Ratings
  - Pricing
  - Facilities
  - Nearby locations
- 🎨 Simple and visually pleasing HTML/CSS user interface.

---

## 📸 Screenshots

<img width="1280" height="800" alt="Main_page" src="https://github.com/user-attachments/assets/6de33387-69b3-4dbd-8d88-5017a66678d8" />

<img width="500" height="600" alt="place_final" src="https://github.com/user-attachments/assets/cac4054c-a15a-48c1-8604-f5cf6570c897" />   

<img width="500" height="700" alt="hotel_final" src="https://github.com/user-attachments/assets/8119839c-7edd-4d8a-bf59-a9f8d48aa5da" />





---

## ✅ Conclusion

This project demonstrates how **content-based filtering** and **price-based ranking** can be used to build a functional and intelligent **tourism recommendation system**. By leveraging key features like category, rating, and price, the system delivers results that align with user expectations and help make informed travel decisions.

---

## 🔮 Future Scope

- 🔁 Add collaborative filtering for user-specific suggestions  
- 💬 Collect user feedback to fine-tune recommendations  
- 📲 Deploy to cloud platforms (Streamlit, Render, or Heroku)  
- 🧠 Expand into a full-fledged **travel planner** with itinerary suggestions  

---

Thank you for visiting this project!  
⭐ Feel free to fork, use, and contribute!




