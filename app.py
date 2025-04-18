import os
from flask import Flask, render_template, jsonify
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Ensure the app binds to the correct port
port = int(os.environ.get("PORT", 5000))  # Get the port from environment variable or default to 5000

def load_results():
    try:
        df = pd.read_csv("data/results.csv")
        return df.to_dict(orient="records")
    except FileNotFoundError:
        return [{"message": "No data available"}]

@app.route("/")
def home():
    results_df = pd.read_csv("data/results.csv")
    results = results_df.to_dict(orient="records")
    return render_template("index.html", results=results, now=datetime.now())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)  # Ensure it's binding to 0.0.0.0 and the right port

