import streamlit as st # type: ignore

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #8e2de2, #4a00e0);
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
        line-height: 1.7;
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

st.markdown('<div class="title">Custom Exception: InvalidAgeError</div>', unsafe_allow_html=True)

class InvalidAgeError(Exception):
    """Custom Exception for Invalid Age"""
    pass

def check_age(age):
    """Function to check if age is less than 18"""
    if age < 18:
        raise InvalidAgeError("Age must be at least 18!")


st.subheader("Enter Your Age to Check If Valid")

st.write("""
In this example, we create a custom exception `InvalidAgeError` to validate the age entered by the user. 
If the age is less than 18, the exception is raised. We handle the exception with a `try...except` block.
""")

# Get the user's age as input
age = st.number_input("Enter your age:", min_value=0, value=18, step=1)

# Try to check the age and raise an exception if necessary
try:
    check_age(age)
    st.markdown(f'<div class="output">Age {age} is valid. You are allowed to proceed!</div>', unsafe_allow_html=True)
except InvalidAgeError as e:
    st.markdown(f'<div class="output">Error: {e}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
