# Import compatibility layer first
import compat  # This must be imported before any other imports

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, request, jsonify, send_from_directory
import util
import os

app = Flask(__name__, static_folder=None)  # Disable static file handling by Flask

# Enable CORS for all routes
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,X-Requested-With')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

# Handle OPTIONS method for CORS preflight
@app.after_request
def after_request(response):
    response = add_cors_headers(response)
    return response

# Handle preflight request
@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        res = jsonify({})
        res = add_cors_headers(res)
        return res, 200

@app.route('/', methods=['GET'])
def home():
    """Root endpoint that provides API documentation"""
    return """
    <h1>House Price Prediction API</h1>
    <p>Welcome to the House Price Prediction API. Available endpoints:</p>
    <ul>
        <li><strong>GET /get_location_names</strong> - Get list of available locations</li>
        <li><strong>POST /predict_home_price</strong> - Predict house price (requires: total_sqft, location, bhk, bath)</li>
    </ul>
    <p>To use this API, make requests to the endpoints above with the required parameters.</p>
    """

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
