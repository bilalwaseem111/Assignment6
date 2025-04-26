import streamlit as st # type: ignore
import time

# Custom CSS Styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(145deg, #1d2b64, #f8cdda);
        font-family: 'Segoe UI', sans-serif;
    }
    .main-title {
        text-align: center;
        font-size: 3em;
        color: grey;
        margin-top: 20px;
        animation: glow 2s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from {
            text-shadow: 0 0 10px #f0f, 0 0 20px #0ff;
        }
        to {
            text-shadow: 0 0 20px #ff0, 0 0 30px #0ff;
        }
    }
    .box {
        background: rgba(255, 255, 255, 0.08);
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
        font-size: 1.5em;
        font-weight: bold;
        animation: fadeIn 2s ease-in;
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
        from {transform: translateY(50px); opacity: 0;}
        to {transform: translateY(0); opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

# Main heading
st.markdown('<div class="main-title">MathUtils & Static Method: Add Two Numbers</div>', unsafe_allow_html=True)

# MathUtils class with static method
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Input Box

num1 = st.text_input("Enter First Number", placeholder="e.g. 12")
num2 = st.text_input("Enter Second Number", placeholder="e.g. 8")
st.markdown('</div>', unsafe_allow_html=True)

# On Click: Add
if st.button("Calculate Sum"):
    if not num1.strip() or not num2.strip():
        st.warning("Please enter both numbers.")
    else:
        try:
            a = float(num1)
            b = float(num2)
            with st.spinner("Calculating..."):
                time.sleep(1.2)
            result = MathUtils.add(a, b)
            st.markdown(f'<div class="output-box">Sum: {result}</div>', unsafe_allow_html=True)
        except ValueError:
            st.error("Invalid input. Please enter valid numbers.")

# Footer
st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
