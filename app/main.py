from flask import Flask, jsonify # type: ignore
from pymongo import MongoClient # type: ignore

app = Flask(__name__)
client = MongoClient("mongodb://admin:password@db-for-app:27017/")
db = client["mydatabase"]

@app.route("/")
def home():
    return jsonify({"status": "Hello from Docker!", "db": "MongoDB connected"})

@app.route("/users")
def users():
    users = list(db.users.find({}, {"_id": 0}))
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)