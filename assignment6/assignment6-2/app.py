import streamlit as st # type: ignore
import time

# CSS styling
st.markdown("""
    <style>
    body {
        background-color: #1e1e2f;
        background-image: linear-gradient(to right, #232526, #414345);
        font-family: 'Segoe UI', sans-serif;
    }
    .main-title {
        text-align: center;
        font-size: 3em;
        color: black;
        margin-top: 20px;
        animation: fadeIn 1s ease-in-out;
    }
    .box {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 15px;
        padding: 30px;
        margin: 30px auto;
        width: 90%;
        max-width: 550px;
        box-shadow: 0 0 25px rgba(0,255,150,0.3);
        animation: slideIn 2s ease;
    }
    .output-box {
        background: rgba(255, 255, 255, 0.15);
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        color: red;
        text-align: center;
        font-size: 1.3em;
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
st.markdown('<div class="main-title"> Object Counter App</div>', unsafe_allow_html=True)

# Class with class variable and method using cls
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

# Session state to store created objects
if 'objects' not in st.session_state:
    st.session_state.objects = []

# Input Box

st.write("Click the button to create a new Counter object.")
if st.button("➕ Create Counter Object"):
    with st.spinner("Creating object..."):
        time.sleep(1)
    new_object = Counter()
    st.session_state.objects.append(new_object)

# Output
if st.session_state.objects:
    st.markdown(f"""
        <div class="output-box">
            Total Counter Objects Created: <b>{Counter.get_count()}</b><br>
            Unique Object IDs: {[id(obj) for obj in st.session_state.objects]}
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown('<div class="output-box">No objects created yet.</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
