from flask import Flask, jsonify #type:ignore
from pymongo import MongoClient #type:ignore
import os

app = Flask(__name__)

# Get connection details from environment
client = MongoClient(
    f"mongodb://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASS')}"
    f"@{os.getenv('MONGO_HOST')}:27017/"
)

@app.route("/")
def home():
    return jsonify({"status": "Hello from Docker!", "db": "MongoDB connected"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)