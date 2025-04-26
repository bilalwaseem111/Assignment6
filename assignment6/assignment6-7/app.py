import streamlit as st # type: ignore
import time

# Custom CSS
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #232526, #414345);
        font-family: 'Segoe UI', sans-serif;
    }
    .main-title {
        text-align: center;
        font-size: 2.8em;
        color: Brown;
        margin-top: 20px;
        animation: glow 2s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from {text-shadow: 0 0 10px #f0f, 0 0 20px #0ff;}
        to {text-shadow: 0 0 20px #ff0, 0 0 30px #0ff;}
    }
    .box {
        background: rgba(255, 255, 255, 0.07);
        border-radius: 15px;
        padding: 30px;
        margin: 30px auto;
        width: 90%;
        max-width: 600px;
        box-shadow: 0 0 25px rgba(255,255,255,0.1);
        animation: slideIn 1.5s ease;
    }
    .output-box {
        background: rgba(255, 255, 255, 0.12);
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        color: black;
        text-align: left;
        font-size: 1.2em;
        font-weight: 500;
        line-height: 1.8;
    }
    .footer {
        text-align: center;
        color: black;
        margin-top: 60px;
        font-weight: bold;
        font-size: 18px;
        animation: fadeIn 3s ease-in;
    }
    @keyframes slideIn {
        from {transform: translateY(40px); opacity: 0;}
        to {transform: translateY(0); opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title"> Employee Class & Access Modifiers Demo</div>', unsafe_allow_html=True)

# Employee class
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name              # public
        self._salary = salary         # protected
        self.__ssn = ssn              # private

    def access_private(self):
        return self.__ssn             # internal access

name = st.text_input("Enter Employee Name", placeholder="e.g. Ahsan")
salary = st.text_input("Enter Salary", placeholder="e.g. 70000")
ssn = st.text_input("Enter SSN (Private)", placeholder="e.g. 123-45-6789")
st.markdown('</div>', unsafe_allow_html=True)

# Access check
if st.button("Access Variables"):
    if not name.strip() or not salary.strip() or not ssn.strip():
        st.warning("Please fill all fields.")
    else:
        try:
            emp = Employee(name, float(salary), ssn)

            # Try accessing all
            public_access = emp.name
            protected_access = emp._salary
            try:
                private_access = emp.__ssn
            except AttributeError:
                private_access = "❌ Cannot access directly (AttributeError)"
            internal_private = emp.access_private()

            st.markdown(f"""
                <div class="output-box">
                     <b>Public Variable (name):</b> {public_access}<br>
                     <b>Protected Variable (_salary):</b> {protected_access}<br>
                     <b>Private Variable (__ssn):</b> {private_access}<br>
                     <b>Private Access via Method:</b> {internal_private}
                </div>
            """, unsafe_allow_html=True)
        except ValueError:
            st.error("Please enter a valid number for salary.")

# Footer
st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
