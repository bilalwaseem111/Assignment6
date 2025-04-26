import streamlit as st # type: ignore


st.markdown("""
    <style>
    body {
        background: linear-gradient(185deg, #ff9a9e, #fad0c4);
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 2.8em;
        text-align: center;
        font-weight: bold;
        color: Brown;
        margin-top: 20px;
        animation: glow 2s infinite alternate;
    }
    @keyframes glow {
        0% {text-shadow: 0 0 5px #ff6ec4, 0 0 10px #ff6ec4;}
        100% {text-shadow: 0 0 20px #f9f871, 0 0 30px #f9f871;}
    }
    .container {
        background: rgba(255, 255, 255, 0.15);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 0px 30px rgba(0,0,0,0.3);
        max-width: 700px;
        margin: 30px auto;
        animation: slideIn 1s ease-out;
    }
    @keyframes slideIn {
        from {opacity: 0; transform: translateY(-40px);}
        to {opacity: 1; transform: translateY(0);}
    }
    .output {
        margin-top: 20px;
        padding: 20px;
        border-radius: 15px;
        background-color: rgba(0, 0, 0, 0.7);
        color: red;
        font-size: 1.3em;
        text-align: center;
        line-height: 1.6;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 18px;
        color: black;
        font-weight: bold;
        animation: fadeIn 2s ease-in-out;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown('<div class="title"> Department and Employee (Aggregation)</div>', unsafe_allow_html=True)


class Employee:
    def __init__(self, emp_name, emp_id):
        self.emp_name = emp_name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee Name: {self.emp_name}<br>Employee ID: {self.emp_id}"

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee

    def department_details(self):
        return f"Department: {self.dept_name}<br>{self.employee.get_details()}"



st.subheader("Create an Employee ")
emp_name = st.text_input("Enter Employee Name:", "Bilal Waseem")
emp_id = st.text_input("Enter Employee ID:", "EMP001")

st.subheader("Assign to a Department ")
dept_name = st.text_input("Enter Department Name:", "Software Development")

st.markdown('</div>', unsafe_allow_html=True)


if st.button("Assign Employee to Department"):
    employee = Employee(emp_name, emp_id)
    department = Department(dept_name, employee)

    st.markdown(f'<div class="output">{department.department_details()}</div>', unsafe_allow_html=True)

\
st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
