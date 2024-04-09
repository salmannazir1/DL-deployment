#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:27:27 2024

@author: mmx
"""


# app.py for Streamlit
import streamlit as st
import requests

st.title('Model Prediction')
user_input = st.text_input("Enter input for model")

if st.button('Predict'):
    response = requests.post('http://localhost:5000/predict', json={'input': user_input})
    st.write(response.json())

