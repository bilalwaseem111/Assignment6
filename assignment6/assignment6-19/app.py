import streamlit as st # type: ignore

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #00bfff, #ff1493);
        font-family: 'Arial', sans-serif;
    }
    .title {
        font-size: 3em;
        text-align: center;
        font-weight: bold;
        color: grey;
        margin-top: 20px;
        animation: colorChange 4s infinite alternate;
    }
    @keyframes colorChange {
        0% {text-shadow: 0 0 10px #ffffff, 0 0 20px #00bfff;}
        100% {text-shadow: 0 0 10px #FFD700, 0 0 20px #ff1493;}
    }
    .container {
        background: rgba(0, 0, 0, 0.7);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 0px 25px rgba(0,0,0,0.5);
        max-width: 800px;
        margin: 30px auto;
        animation: slideIn 1.5s ease-in-out;
    }
    @keyframes slideIn {
        from {opacity: 0; transform: translateY(-50px);}
        to {opacity: 1; transform: translateY(0);}
    }
    .output {
        margin-top: 20px;
        padding: 20px;
        border-radius: 15px;
        color: red;
        font-size: 1.5em;
        text-align: center;
        line-height: 1.7;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 18px;
        color: black;
        font-weight: bold;
        animation: fadeIn 2s ease-in-out;
    }
    @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)


st.markdown('<div class="title">Callable() and __call__()</div>', unsafe_allow_html=True)

class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Store the multiplication factor
    
    # __call__ method allows the object to be called like a function
    def __call__(self, value):
        return value * self.factor

st.subheader("Testing Callable and __call__()")
st.write("""
In this example, we create a `Multiplier` class with an `__init__()` method to set a multiplication factor. 
The `__call__()` method makes the object callable, allowing us to use the object like a function. 
We'll test this with both `callable()` and by calling the object directly.
""")

# Create a Multiplier object with a factor of 5
multiplier = Multiplier(5)

# Check if the multiplier object is callable
is_callable = callable(multiplier)
st.markdown(f'<div class="output">Is the multiplier callable? {is_callable}</div>', unsafe_allow_html=True)

# Use the multiplier object like a function
input_value = st.number_input("Enter a value to multiply:", min_value=1, value=2)
result = multiplier(input_value)  # Call the object as a function
st.markdown(f'<div class="output">Result of multiplying {input_value} by {multiplier.factor}: {result}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
