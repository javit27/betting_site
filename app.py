import os
from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

def load_results():
    try:
        df = pd.read_csv("data/results.csv")  # Load the CSV file containing results
        return df.to_dict(orient="records")   # Convert DataFrame to a list of dictionaries
    except FileNotFoundError:
        return [{"message": "No data available"}]  # Return this if the CSV is missing

def load_historical_results():
    try:
        # Assuming you have a 'historical_results.csv' file
        df = pd.read_csv("data/historical_results.csv")
        return df.to_dict(orient="records")  # Convert the DataFrame to a list of dictionaries
    except FileNotFoundError:
        return [{"message": "No historical data available"}]  # Return a message if the CSV is missing

@app.route("/")
def home():
    results = load_results()  # Get the results
    return render_template("index.html", results=results)  # Pass results to the template

@app.route("/historical")
def historical():
    historical_results = load_historical_results()  # Load historical data
    return render_template("historical.html", results=historical_results)

@app.route("/api/results")
def results():
    return jsonify(load_results())  # Return results as JSON (for API calls)

if __name__ == "__main__":
    # Get the port from the environment variable, default to 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
