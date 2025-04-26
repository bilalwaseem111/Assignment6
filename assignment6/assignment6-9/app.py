import streamlit as st # type: ignore
from abc import ABC, abstractmethod

# Custom CSS for animations and style
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #1c1c2b, #2d2d44);
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 2.5em;
        color: Blue;
        margin: 20px 0;
        animation: glow 2s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from { text-shadow: 0 0 10px #0ff, 0 0 20px #0ff; }
        to { text-shadow: 0 0 20px #f0f, 0 0 30px #0ff; }
    }
    .box {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 30px;
        margin: 30px auto;
        width: 90%;
        max-width: 600px;
        box-shadow: 0 0 25px rgba(255,255,255,0.1);
        animation: fadeIn 1.5s ease;
    }
    .output {
        margin-top: 20px;
        padding: 20px;
        background-color: rgba(255,255,255,0.12);
        color: Grey;
        border-radius: 12px;
        font-size: 1.2em;
        font-weight: 500;
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
        from {opacity: 0; transform: translateY(40px);}
        to {opacity: 1; transform: translateY(0);}
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title"> Area Calculator by Abstract Class</div>', unsafe_allow_html=True)

# Abstract Class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Rectangle Class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Input Form

shape_type = st.selectbox("Choose Shape", ["Rectangle", "Coming Soon..."])
length = st.number_input("Enter Length", min_value=0.0, format="%.2f")
width = st.number_input("Enter Width", min_value=0.0, format="%.2f")
st.markdown('</div>', unsafe_allow_html=True)

# Calculate Area
if st.button("Calculate Area"):
    if shape_type == "Rectangle":
        if length == 0 or width == 0:
            st.warning("Both length and width must be greater than 0.")
        else:
            rect = Rectangle(length, width)
            area_result = rect.area()
            st.markdown(f'<div class="output">📏 Length: {length} units<br>📐 Width: {width} units<br>🟦 Area: {area_result:.2f} square units</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
