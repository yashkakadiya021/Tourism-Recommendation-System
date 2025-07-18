
from flask import Flask, render_template, request, render_template_string
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load datasets
places = pd.read_csv('final_places.csv')
hotels = pd.read_csv('final_hotel.csv')
hotel_cities = sorted(hotels['destination name'].dropna().unique())

# Destination Recommendation Setup
places['combined'] = places['category'] + ' ' + places['city']
tfidf = TfidfVectorizer(stop_words='english')
place_vectors = tfidf.fit_transform(places['combined'])

@app.route('/')
def home():
    hotel_city_options = ''.join([f'<option value="{city}">{city}</option>' for city in hotel_cities])
    html = f"""
    <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tourism Recommendation System</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-image: url('/static/6346166.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }}
        .navbar {{
            background-color: #333;
            color: white;
            padding: 15px;
            text-align: center;
            width: 40%;
            font-size: 1.5em;
            margin-bottom: 20px;
        }}
        form {{
            background-color: #fff;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
            width: 350px;
            text-align: center;
            transition: transform 0.3s ease;
        }}
        form:hover {{
            transform: scale(1.02);
        }}
        input, select, button {{
            width: 90%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #888;
            font-size: 1em;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
            transition: 0.3s;
        }}
        input:hover, select:hover {{
            border-color: #4CAF50;
            box-shadow: 0 0 5px #4CAF50;
        }}
        input:focus, select:focus {{
            outline: none;
            border-color: #4CAF50;
            box-shadow: 0 0 8px #4CAF50;
        }}
        button {{
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
            border: none;
        }}
        button:hover {{
            background-color: #45a049;
            transform: scale(1.05);
            box-shadow: 0px 6px 12px rgba(0,0,0,0.2);
        }}
        .card {{
            background: #fff;
            padding: 15px;
            margin: 10px 0;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            width: 600px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
        }}
    </style>
</head>
<body>
    <div class="navbar">Tourism Recommendation System</div>

    <h2>Destination Recommendation</h2>
    <form action="/destination" method="post">
        <select name="category" required>
            <option value="" disabled selected>Select a Category</option>
            <option value="Wildlife/Nature">Wildlife/Nature</option>
            <option value="Historical">Historical</option>
            <option value="Beaches">Beaches</option>
            <option value="Urban/Modern">Urban/Modern</option>
            <option value="Lakes/Rivers">Lakes/Rivers</option>
            <option value="Adventure">Adventure</option>
            <option value="Mountains">Mountains</option>
            <option value="Temple">Temple</option>
            <option value="Other">Other</option>
            <option value="Spiritual">Spiritual</option>
        </select>
        <button type="submit">Get Destination Recommendations</button>
    </form>

    <h2>Hotel Recommendation</h2>
    <form action="/hotel" method="post">
        <select name="hotel_city" required>
            <option value="" disabled selected>Select a City</option>
            {hotel_city_options}
        </select>
        <input type="number" name="max_price" placeholder="Max price" required>
        <button type="submit">Get Hotel Recommendations</button>
    </form>
</body>
</html>
    """
    return html

# The rest of your routes (destination and hotel) stay unchanged.



    return render_template('home.html', hotel_cities=hotel_city_options)


@app.route('/destination', methods=['POST'])
def destination_recommend():
    category = request.form.get('category')
    filtered_places = places[places['category'].str.strip().str.lower() == category.strip().lower()]
    if not filtered_places.empty:
        recommendations = filtered_places.sort_values(by='Rating', ascending=False).head(10)
        html = """
        <html>
        <head>
            <title>Recommended Destinations</title>
            <style>
                body {
                    font-family: Arial, sans serif;
                    background-image: url('/static/bg-destination.jpg');
                    background-size: cover;
                    background-position: center;
                    background-repeat: no-repeat;
                    margin: 0;
                    padding: 20px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    flex-direction: column;
                }
                .card {
                    background: rgba(255, 255, 255, 0.9);
                    color: black;
                    padding: 15px;
                    margin: 10px 0;
                    border-radius: 8px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.5);
                    width: 600px;
                }
                a {
                    color: yellow;
                    text-decoration: none;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
        <div style='display: flex; flex-direction: column; align-items: center;'>
        <h2>Recommended Destinations (Top Rated):</h2>"""

        for _, row in recommendations.iterrows():
            html += "<div class='card'>"
            html += f"<h3>{row['places name']}</h3>"
            html += f"<p><strong>Category:</strong> {row['category']}</p>"
            html += f"<p><strong>City:</strong> {row['city']}</p>"
            html += f"<p><strong>Rating:</strong> ⭐ {row['Rating']}</p>"
            html += f"<p>{row['places description']}</p>"
            html += "</div>"
        html += '</div><br><a href="/">Back to Home</a></body></html>'
        return html
    else:
        return 'No destinations found. <br><a href="/">Back to Home</a>'

# @app.route('/destination', methods=['POST'])
# def destination_recommend():
#     category = request.form.get('category')
#     filtered_places = places[places['category'].str.strip().str.lower() == category.strip().lower()]
#     if not filtered_places.empty:
#         recommendations = filtered_places.sort_values(by='Rating', ascending=False).head(10)

#         html = """
# <div style='display: flex; flex-direction: column; align-items: center;'>
# <h2>Recommended Destinations (Top Rated):</h2>"""
#         for _, row in recommendations.iterrows():
#             html += "<div style='background:#fff; padding:15px; margin:10px 0; border-radius:8px;"
#             html += "box-shadow:0 2px 5px rgba(0,0,0,0.5); width: 600px;'>"
#             html += f"<h3 style='margin-bottom:5px;'>{row['places name']}</h3>"
#             html += f"<p><strong>Category:</strong> {row['category']}</p>"
#             html += f"<p><strong>City:</strong> {row['city']}</p>"
#             html += f"<p><strong>Rating:</strong> ⭐ {row['Rating']}</p>"
#             html += f"<p style='color:#555;'>{row['places description']}</p>"
#             html += "</div>"
#         html += '</div><br><a href="/">Back to Home</a>'
#         return html
#     else:
#         return 'No destinations found. <br><a href="/">Back to Home</a>'



@app.route('/hotel', methods=['POST'])
def hotel_recommend():
    hotel_city = request.form.get('hotel_city')
    max_price = float(request.form.get('max_price'))

    scaler_rating = MinMaxScaler()
    scaler_price = MinMaxScaler()
    hotels['normalized_rating'] = scaler_rating.fit_transform(hotels[['rating']])
    hotels['inverse_price'] = scaler_price.fit_transform(1 / hotels[['discount price']])
    hotels['score'] = 0.7 * hotels['normalized_rating'] + 0.3 * hotels['inverse_price']

    filtered_hotels = hotels[
        (hotels['destination name'].str.contains(hotel_city, case=False, na=False)) &
        (hotels['discount price'] <= max_price)
    ]

    if not filtered_hotels.empty:
        hotel_recommendations = filtered_hotels.sort_values(by='score', ascending=False).head(10)

        html = """
        <html>
        <head>
            <title>Recommended Hotels</title>
            <style>
                body {
                    background-image: url('/static/bg-hotel.jpg');
                    background-size: cover;
                    background-position: center;
                    background-repeat: no-repeat;
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 20px;
                    color: white;
                }
                .card {
                    background: rgba(255, 255, 255, 0.9);
                    color: black;
                    padding: 15px;
                    margin: 10px 0;
                    border-radius: 8px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.5);
                    width: 600px;
                }
                a {
                    color: yellow;
                    text-decoration: none;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
        <div style='display: flex; flex-direction: column; align-items: center;'>
        <h2 style="color: black;">Recommended Hotels:</h2>"""

        for _, row in hotel_recommendations.iterrows():
            facilities = [f.strip() for f in str(row['facilities']).split(',')] if pd.notna(row['facilities']) else []
            nearby = row['near by place'] if pd.notna(row['near by place']) else "N/A"

            html += "<div class='card'>"
            html += f"<h3>{row['hotel name']}</h3>"
            html += f"<p><strong>Rating:</strong> ⭐ {row['rating']}</p>"
            html += f"<p><strong>Original Price:</strong> ₹{row['actual price']}</p>"
            html += f"<p><strong>Discounted Price:</strong> <span style='color:lightgreen;'>₹{row['discount price']}</span></p>"
            html += f"<p><strong>📍 Distance:</strong> {nearby}</p>"

            if facilities:
                html += "<p><strong>Facilities:</strong></p><ul>"
                for f in facilities:
                    html += f"<li>{f}</li>"
                html += "</ul>"

            html += "</div>"

        html += '</div><br><a href="/">Back to Home</a></body></html>'
        return html
    else:
        return 'No hotels found. <br><a href="/">Back to Home</a>'


# @app.route('/hotel', methods=['POST'])
# def hotel_recommend():
#     hotel_city = request.form.get('hotel_city')
#     max_price = float(request.form.get('max_price'))

#     scaler_rating = MinMaxScaler()
#     scaler_price = MinMaxScaler()
#     hotels['normalized_rating'] = scaler_rating.fit_transform(hotels[['rating']])
#     hotels['inverse_price'] = scaler_price.fit_transform(1 / hotels[['discount price']])
#     hotels['score'] = 0.7 * hotels['normalized_rating'] + 0.3 * hotels['inverse_price']

#     filtered_hotels = hotels[
#         (hotels['destination name'].str.contains(hotel_city, case=False, na=False)) &
#         (hotels['discount price'] <= max_price)
#     ]

#     if not filtered_hotels.empty:
#         hotel_recommendations = filtered_hotels.sort_values(by='score', ascending=False).head(10)

#         html = """
# <div style='display: flex; flex-direction: column; align-items: center;'>
# <h2>Recommended Hotels:</h2>"""
#         for _, row in hotel_recommendations.iterrows():
#             facilities = [f.strip() for f in str(row['facilities']).split(',')] if pd.notna(row['facilities']) else []
#             nearby = row['near by place'] if pd.notna(row['near by place']) else "N/A"

#             html += "<div style='background:#fff; padding:15px; margin:10px 0; border-radius:8px;"
#             html += "box-shadow:0 2px 5px rgba(0,0,0,0.5); width: 600px;'>"
#             html += f"<h3 style='margin-bottom:5px;'>{row['hotel name']}</h3>"
#             html += f"<p><strong>Rating:</strong> ⭐ {row['rating']}</p>"
#             html += f"<p><strong>Original Price:</strong> ₹{row['actual price']}</p>"
#             html += f"<p><strong>Discounted Price:</strong> <span style='color:green;'>₹{row['discount price']}</span></p>"
#             html += f"<p><strong>📍 Distance:</strong> {nearby}</p>"

#             if facilities:
#                 html += "<p><strong>Facilities:</strong></p><ul>"
#                 for f in facilities:
#                     html += f"<li>{f}</li>"
#                 html += "</ul>"

#             html += "</div>"

#         html += '</div><br><a href="/">Back to Home</a>'
#         return html
#     else:
#         return 'No hotels found. <br><a href="/">Back to Home</a>'


if __name__ == '__main__':
    app.run(debug=True)
