#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:24:22 2024

@author: mmx
"""

from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model('/Users/mmx/Downloads/trained_model.sav')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['input']])
    return jsonify(prediction.tolist())

if __name__ == '__main__':
    app.run(port=5000, debug=True)