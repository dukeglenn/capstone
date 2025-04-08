import streamlit as st
import os
import pickle
import numpy as np
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'model.pkl')

# Load the model
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# def predict_negligence()

# Set the page layout to wide
st.set_page_config(page_title="Astraea", layout="wide")

st.markdown("""
    <style>
        body {
            background-color: #2b576d !important;
        }
    </style>
""", unsafe_allow_html=True)

# Custom CSS for styling the navbar and adding a 100px buffer at the top
st.markdown("""
    <style>
        /* Ensure body has no margin/padding */
        body {
            margin: 0;
            padding: 0;
        }

        /* Navbar Styling */
        .topnav {
            background-color: #031a2d;
            overflow: hidden;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            padding: 10px 20px;
            width: 100%;
        }

        .topnav a {
            color: white;
            text-decoration: none;
            padding: 14px 16px;
            font-size: 17px;
            font-weight: bold;
            transition: background-color 0.3s, color 0.3s;
        }

        .topnav a:hover {
            background-color: #efcf96;
            color: #031a2d;
        }

        .topnav a.active {
            background-color: #4584a4;
            color: white;
        }

        /* Buffer to push everything down, including navbar */
        .main-container {
            margin-top: 10px; /* 10px buffer applied to navbar & content */
        }
    </style>
""", unsafe_allow_html=True)

# Space below navbar to avoid content being hidden
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# Navigation Bar
st.markdown("""
    <div class="topnav">
        <a class="active" href="#">Astraea</a>
        <a href="#">Contact</a>
        <a href="#">About</a>
        <a href="#">Legal Info</a>
    </div>
""", unsafe_allow_html=True)

# Layout with two columns
col1, col2 = st.columns([1, 1])  # Adjust ratio as needed

# Left section - Welcome message
# Left Section - Background Image with Overlay Text
with col1:
    # Load an image (Replace with your actual image path)
    image_url = "Astraea_Logo.png"  # Example image
    st.image(image_url, use_container_width=True)

    # Overlay Text (Placed in a markdown box)
    st.markdown("""
        <div style="
            position: relative; 
            top: -250px; 
            background: rgba(0, 0, 0, 0.6); 
            padding: 20px; 
            border-radius: 10px;
            color: white;
            text-align: center;">
            <h1>Welcome to Astraea</h1>
            <p>
                Astraea is committed to enhancing the legal landscape by harnessing the power of 
                machine learning to provide clear, data-driven insights on legal case outcomes 
                and financial information. We empower individuals and families to make informed 
                decisions and connect them to the right legal solutions and professionals, 
                making justice more accessible and transparent for all.
            </p>
        </div>
    """, unsafe_allow_html=True)
# Right section - User input box
with col2:
    perpVictim = st.selectbox("Did you hit the other car or did you get hit?", ['I got hit', 'I hit them'])

    if perpVictim == 'I got hit':
        victimNegligence = st.selectbox("Were you negligent?", ['Yes', 'No'])
        victimEmDoc = st.selectbox("Were you faced with an emergency?", ['Yes', 'No'])
        victimInjury = st.selectbox("Were you seriously injured?", ['Yes', 'No'])
        perpNegligence = st.selectbox("Were they negligent?", ['Yes', 'No'])
        perpEmDoc = st.selectbox("Were they faced with an emergency?", ['Yes', 'No'])
        perpInjury = st.selectbox("Were they seriously injured?", ['Yes', 'No'])
    elif perpVictim == 'I hit them':
        victimNegligence = st.selectbox("Were they negligent?", ['Yes', 'No'])
        victimEmDoc = st.selectbox("Were they faced with an emergency?", ['Yes', 'No'])
        victimInjury = st.selectbox("Were they seriously injured?", ['Yes', 'No'])
        perpNegligence = st.selectbox("Were you negligent?", ['Yes', 'No'])
        perpEmDoc = st.selectbox("Were you faced with an emergency?", ['Yes', 'No'])
        perpInjury = st.selectbox("Were you seriously injured?", ['Yes', 'No'])

    if st.button("Submit"):
        def convert_to_numeric(value):
            return 1 if value == "Yes" else 0
        
        features = pd.DataFrame({
            'victim_negligence': [convert_to_numeric(victimNegligence)],
            'victim_em_doc': [convert_to_numeric(victimEmDoc)],
            'victim_serious_injury': [convert_to_numeric(victimInjury)],
            'perp_negligence': [convert_to_numeric(perpNegligence)],
            'perp_em_doc': [convert_to_numeric(perpEmDoc)],
            'perp_serious_injury': [convert_to_numeric(perpInjury)]
        })
        prediction = model.predict(features)
        st.success(f"Prediction: {prediction[0]}")