import streamlit as st # type: ignore
import time

# CSS Styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #2c3e50, #4ca1af);
        font-family: 'Segoe UI', sans-serif;
    }
    .main-title {
        text-align: center;
        font-size: 3em;
        color: dark green;
        margin-top: 20px;
        animation: fadeIn 2s ease-in-out;
    }
    .box {
        background: rgba(255, 255, 255, 0.07);
        border-radius: 15px;
        padding: 30px;
        margin: 30px auto;
        width: 90%;
        max-width: 500px;
        box-shadow: 0 0 25px rgba(255,255,255,0.2);
        animation: slideIn 2s ease;
    }
    .output-box {
        background: rgba(255, 255, 255, 0.15);
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        color: black;
        text-align: center;
        font-size: 1.2em;
    }
    .footer {
        text-align: center;
        color: black;
        margin-top: 60px;
        font-weight: bold;
        font-size: 18px;
        animation: fadeIn 3s ease-in;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    @keyframes slideIn {
        from {transform: translateY(60px); opacity: 0;}
        to {transform: translateY(0); opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">Car Class & Public Variables & Methods</div>', unsafe_allow_html=True)

# Input and logic box

brand = st.text_input("Enter Car Brand", placeholder="e.g. Toyota, Tesla")
st.markdown('</div>', unsafe_allow_html=True)

# Car class
class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):  # Public method
        return f"The {self.brand} car has started."

# On button click
if st.button("Start Car"):
    if brand.strip() == "":
        st.warning("Please enter a car brand first.")
    else:
        with st.spinner("Starting the car..."):
            time.sleep(1.5)
        car = Car(brand)
        output = f"Brand: {car.brand}<br>{car.start()}"
        st.markdown(f'<div class="output-box">{output}</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
