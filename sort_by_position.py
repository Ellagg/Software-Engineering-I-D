from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
from pymongo import MongoClient

app = Flask(__name__)

CONNECTION_STRING = 

client = MongoClient(CONNECTION_STRING)
db = client["SoftwareEngineeringI"]
collection = db["players"]

# Sort by position
@app.route("/sort-by-position", methods=["GET"])
def position():
    position = request.args.get('position')

    players = list(collection.find({"position": position}, {"_id": 0})) 
    
    if not players:
        return jsonify({"message": "No players found for this position"}), 404

    return jsonify(players)

if __name__ == "__main__":
    app.run(port = 5000, debug = True)