from flask import Flask, render_template, request, jsonify
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

# Dummy function to simulate stock price predictions
def predict_stock_price(ticker):
    # Simulating prediction logic
    # In a real application, replace this with your model prediction code
    model = Sequential([
        Dense(50, activation='relu', input_dim=1),
        Dense(1)
    ])
    
    # Load pre-trained model weights (if available)
    # model.load_weights('best_model.keras') 
    
    # Placeholder predictions - Replace with real model prediction
    predicted_prices = np.random.rand(4) * 100  # Example: 4 random predicted prices
    
    return predicted_prices.tolist()

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle stock price prediction
@app.route('/predict', methods=['GET'])
def predict():
    ticker = request.args.get('ticker')
    predictions = predict_stock_price(ticker)
    return jsonify({'prices': predictions})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
