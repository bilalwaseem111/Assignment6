import streamlit as st # type: ignore


st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #FFB6C1, #FFD700);
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
        0% {text-shadow: 0 0 10px #ff6347, 0 0 20px #ff4500;}
        100% {text-shadow: 0 0 20px #f0e68c, 0 0 30px #ffd700;}
    }
    .container {
        background: rgba(0, 0, 0, 0.5);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 0px 25px rgba(0,0,0,0.5);
        max-width: 750px;
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
        background-color: rgba(0, 0, 0, 0.8);
        color: green;
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

st.markdown('<div class="title">Function Decorators: log_function_call</div>', unsafe_allow_html=True)

def log_function_call(func):
    def wrapper(*args, **kwargs):
        st.write("Function is being called")
        return func(*args, **kwargs)
    return wrapper


@log_function_call
def say_hello():
    return "Hello, welcome to the world of decorators!"

st.subheader("Understanding Decorators ")
st.write("""
A **decorator** is a function that adds functionality to an existing function. In this case, we use the decorator `log_function_call` to log a message before calling the function `say_hello`.
""")

if st.button("Call the decorated function"):
    result = say_hello()
    st.markdown(f'<div class="output">{result}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
