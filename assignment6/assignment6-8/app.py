import streamlit as st # type: ignore

# Custom CSS
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #1e1e2f, #2d2d44);
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 2.5em;
        color: Brown;
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
        color: grey;
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
st.markdown('<div class="title"> Teacher Registration using super()</div>', unsafe_allow_html=True)

# Classes
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        return f"👤 Name: {self.name}\n📘 Subject: {self.subject}"

# Input Form

name = st.text_input("Enter Teacher Name", placeholder="e.g. Zara")
subjects = ["Mathematics", "Physics", "Chemistry", "Biology", "English", "Computer Science", "History"]
subject = st.selectbox("Select Subject", subjects)
st.markdown('</div>', unsafe_allow_html=True)

# Show Output
if st.button("Register Teacher"):
    if not name.strip():
        st.warning("Please enter the teacher's name.")
    else:
        t = Teacher(name, subject)
        html_output = t.display().replace("\n", "<br>")
        st.markdown(f'<div class="output">{html_output}</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
