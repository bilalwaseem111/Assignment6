import streamlit as st # type: ignore
import time

# CSS styling
st.markdown("""
    <style>
    body {
        background-color: #0f2027;
        background-image: linear-gradient(to right, #2c5364, #203a43, #0f2027);
        font-family: 'Segoe UI', sans-serif;
    }
    .main-title {
        text-align: center;
        font-size: 3em;
       color: black;
        margin-top: 20px;
        
    }
    .box {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 30px;
        margin: 30px auto;
        width: 90%;
        max-width: 500px;
        box-shadow: 0 0 20px rgba(0,255,255,0.3);
        animation: slideIn 2s ease;
    }
    .output-box {
        background: rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        color: #ffffff;
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
        from {transform: translateY(50px); opacity: 0;}
        to {transform: translateY(0); opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">Student Info App</div>', unsafe_allow_html=True)

# Input area
with st.container():
 
    name = st.text_input("Enter Student Name")
    marks = st.number_input("Enter Marks", min_value=0, max_value=100)
    st.markdown('</div>', unsafe_allow_html=True)

    class Student:
        def __init__(self, name, marks):
            self.name = name
            self.marks = marks

        def display(self):
            return f"Name: {self.name}\nMarks: {self.marks}"

    if st.button("Show Student Details"):
        with st.spinner("Loading..."):
            time.sleep(1.5)
        student = Student(name, marks)
        output_html = student.display().replace("\n", "<br>")
        st.markdown(f'<div class="output-box">{output_html}</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
