import streamlit as st # type: ignore
import time

st.markdown("""
<style>
body {
    background: linear-gradient(to right, #1e3c72, #2a5298);
    font-family: 'Segoe UI', sans-serif;
}
.title {
    font-size: 3em;
    color: brown;
    text-align: center;
    font-weight: bold;
    animation: fadeInDown 2s ease-in-out;
    margin-top: 30px;
}
@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-30px); }
    to { opacity: 1; transform: translateY(0); }
}
.card {
    background-color: rgba(255,255,255,0.1);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 0 20px rgba(0,0,0,0.5);
    max-width: 800px;
    margin: auto;
    animation: fadeInUp 1.5s ease-in-out;
}
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(40px); }
    to { opacity: 1; transform: translateY(0); }
}
.log-box {
    background-color: pink;
    color: red;
    font-family: 'Courier New', monospace;
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
    text-align: center;
    font-size: 1.2em;
}
.footer {
    text-align: center;
    color: white;
    margin-top: 50px;
    font-weight: bold;
    animation: fadeIn 2s ease-in-out;
}
@keyframes fadeIn {
    0% {opacity: 0;}
    100% {opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Constructors and Destructors in Python</div>', unsafe_allow_html=True)
# st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("Live Logger Simulation")
st.write("This example demonstrates the concept of **constructors** and **destructors** using a class called `Logger`.")
st.write("Press the button below to create and destroy a logger object dynamically.")

class Logger:
    def __init__(self, name):
        self.name = name
        st.markdown(f"<div class='log-box'>Logger Created: {self.name}</div>", unsafe_allow_html=True)

    def __del__(self):
        st.markdown(f"<div class='log-box'>Logger Destroyed: {self.name}</div>", unsafe_allow_html=True)

if 'logger' not in st.session_state:
    st.session_state.logger = None

logger_name = st.text_input("Enter logger name:", value="MyLogger")

if st.button("Create Logger"):
    st.session_state.logger = Logger(logger_name)

if st.button("Delete Logger"):
    st.session_state.logger = None
    st.markdown(f"<div class='log-box'>Logger Object Reference Removed</div>", unsafe_allow_html=True)
    st.experimental_rerun()

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
