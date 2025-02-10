import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Fetch API Key securely from environment variable
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

@app.route("/news", methods=["GET"])
def get_news():
    if not NEWS_API_KEY:
        return jsonify({"error": "API key is missing"}), 500

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch news"}), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
