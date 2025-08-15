from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (important for Android)

# Sample product data
products = {
    "shoes": [
        {
            "id": 1,
            "name": "Nike Air Max Plus",
            "price": "₹14,995",
            "description": "High-quality sports shoes for comfort and performance.",
            "image": "https://static.nike.com/a/images/t_PDP_936_v1/f_auto,q_auto:eco/47b7945e-a379-4c24-b9df-98f4eef178e5/NIKE+AIR+MAX+PLUS.png"
        },
        {
            "id": 2,
            "name": "Adidas Ultraboost 5",
            "price": "₹11,999",
            "description": "High-performance shoes with Boost technology.",
            "image": "https://assets.adidas.com/images/w_600,f_auto,q_auto/59f3f8b61fb146dabf3a48566e6c7fd9_9366/Ultraboost_5_Shoes_Blue_ID8817_HM3_hover.jpg"
        }
    ],
    "bags": [
        {
            "id": 1,
            "name": "Wildcraft Backpack",
            "price": "₹2,499",
            "description": "Spacious backpack for travel and daily use.",
            "image": "https://m.media-amazon.com/images/I/81sMLI5-qtL._SX679_.jpg"
        },
        {
            "id": 2,
            "name": "American Tourister Duffel",
            "price": "₹3,499",
            "description": "Durable duffel bag for short trips.",
            "image": "https://m.media-amazon.com/images/I/71Tz8YET0-L._SX679_.jpg"
        }
    ]
}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Product API"})

@app.route('/products/<category>', methods=['GET'])
def get_products(category):
    category = category.lower()
    if category in products:
        return jsonify(products[category])
    else:
        return jsonify({"error": "Category not found"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
