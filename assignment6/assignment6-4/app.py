import streamlit as st # type: ignore
import time

# Stylish CSS
st.markdown("""
    <style>
    body {
        background: linear-gradient(120deg, #1f1c2c, #928DAB);
        font-family: 'Segoe UI', sans-serif;
    }
    .main-title {
        text-align: center;
        font-size: 4em;
        color: black;
        margin-top: 30px;
        animation: fadeIn 2s ease-in-out;
    }
    .box {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 15px;
        padding: 30px;
        margin: 30px auto;
        width: 90%;
        max-width: 550px;
        box-shadow: 0 0 30px rgba(0,255,255,0.3);
        animation: slideIn 1.5s ease;
    }
    .output-box {
        background: rgba(255, 255, 255, 0.15);
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        color: red;
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
st.markdown('<div class="main-title"> Bank Class & Class Variables & Methods</div>', unsafe_allow_html=True)

# Bank class with class variable and class method
class Bank:
    bank_name = "National Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# UI box

user_name = st.text_input("Enter your name to open a bank account", placeholder="e.g. Ali, Sara")
new_bank_name = st.text_input("Change bank name (optional)", placeholder="e.g. Global Trust Bank")

if st.button("Create Bank Account"):
    if user_name.strip() == "":
        st.warning("Please enter your name.")
    else:
        with st.spinner("Creating account..."):
            time.sleep(1.2)
        user = Bank(user_name)
        st.markdown(f"""
            <div class="output-box">
                Welcome, <b>{user.account_holder}</b>!<br>
                Your bank is: <b>{Bank.bank_name}</b>
            </div>
        """, unsafe_allow_html=True)

if st.button("🔁 Change Bank Name"):
    if new_bank_name.strip() == "":
        st.warning("Please enter a new bank name.")
    else:
        Bank.change_bank_name(new_bank_name)
        st.success(f"Bank name changed to: {Bank.bank_name}")

# Show updated bank name
if Bank.bank_name:
    st.markdown(f"""
        <div class="output-box">
            Current Bank Name: <b>{Bank.bank_name}</b>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
