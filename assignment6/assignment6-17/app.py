import streamlit as st # type: ignore


st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #8A2BE2, #FF6347);
        font-family: 'Arial', sans-serif;
    }
    .title {
        font-size: 3em;
        text-align: center;
        font-weight: bold;
        color: brown;
        margin-top: 20px;
        animation: colorChange 4s infinite alternate;
    }
    @keyframes colorChange {
        0% {text-shadow: 0 0 10px #ffffff, 0 0 20px #8A2BE2;}
        100% {text-shadow: 0 0 10px #FFD700, 0 0 20px #FF6347;}
    }
    .container {
        background: rgba(0, 0, 0, 0.6);
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
        background-color: green
        color: grey;
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


st.markdown('<div class="title">Class Decorators: add_greeting</div>', unsafe_allow_html=True)

def add_greeting(cls):
    # Add a greet method to the class
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        return f"Hello, my name is {self.name}"


st.subheader("Class Decorators in Action ")
st.write("""
A **class decorator** allows us to add or modify methods of a class. In this example, the `add_greeting` decorator adds a `greet()` method that returns a greeting message. The class `Person` is decorated with this decorator, and it can now greet!
""")


person = Person(name="Bilal")

if st.button("Get Greeting from Person"):
    result = person.greet()  # Call the greet() method added by the decorator
    st.markdown(f'<div class="output">{result}</div>', unsafe_allow_html=True)


if st.button("Display Person's Info"):
    info = person.display()
    st.markdown(f'<div class="output">{info}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
