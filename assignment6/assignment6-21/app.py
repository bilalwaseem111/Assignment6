import streamlit as st # type: ignore
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #00c6ff, #0072ff);
        font-family: 'Arial', sans-serif;
    }
    .title {
        font-size: 3.5em;
        text-align: center;
        color: brown;
        font-weight: bold;
        margin-top: 20px;
    }
    @keyframes textGlow {
        0% {text-shadow: 0 0 10px #ff7f50, 0 0 20px #ff7f50;}
        100% {text-shadow: 0 0 20px #ff0000, 0 0 30px #ff0000;}
    }
    .container {
        background: rgba(0, 0, 0, 0.6);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 0px 30px rgba(0,0,0,0.5);
        max-width: 800px;
        margin: 40px auto;
        animation: slideIn 1.5s ease-in-out;
    }
    @keyframes slideIn {
        from {opacity: 0; transform: translateY(-30px);}
        to {opacity: 1; transform: translateY(0);}
    }
    .output {
        margin-top: 20px;
        padding: 20px;
        border-radius: 15px;
        color: red;
        font-size: 1.4em;
        text-align: center;
        line-height: 2.7;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 18px;
        color: #fff;
        font-weight: bold;
        animation: fadeIn 2s ease-in-out;
    }
    @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        current_value = self.current
        self.current -= 1
        return current_value

st.markdown('<div class="title">Countdown: Iterable Example</div>', unsafe_allow_html=True)


st.subheader("Create Your Countdown Timer")

st.write("""
In this example, we create a custom class `Countdown` that makes use of Python's `__iter__` and `__next__` methods to make the class iterable.
This allows you to use the `for` loop directly on instances of the `Countdown` class.
""")

start_number = st.number_input("Enter a start number for the countdown:", min_value=0, value=10, step=1)

# Create Countdown instance
countdown = Countdown(start_number)

# Countdown loop
st.markdown('<div class="output">Countdown starts:</div>', unsafe_allow_html=True)
for value in countdown:
    st.write(value)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
