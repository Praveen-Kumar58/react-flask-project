import os
from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Flask API is running successfully!"

@app.route("/api/facts")
def facts():
    return jsonify([
        {"id": 1, "fact": "The sun is a star."},
        {"id": 2, "fact": "Water boils at 100°C."},
        {"id": 3, "fact": "Earth has one moon."},
        {"id":4,"fact":"The Great Wall of China is visible from space."},
        {"id":5,"fact":"Honey never spoils."},
        {"id":6,"fact":"Octopuses have three hearts."},
        {"id":7,"fact":"Bananas are berries, but strawberries aren't."},
        {"id":8,"fact":"The Eiffel Tower can be 15 cm taller during the summer."},
        {"id":9,"fact":"Sharks have been around longer than trees."},
        {"id":10,"fact":"A group of flamingos is called a 'flamboyance'."}
    ])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
