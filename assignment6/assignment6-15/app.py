import streamlit as st # type: ignore

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #8EC5FC, #E0C3FC);
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 3em;
        text-align: center;
        font-weight: bold;
        color: brown;
        margin-top: 20px;
        animation: colorChange 3s infinite alternate;
    }
    @keyframes colorChange {
        0% {text-shadow: 0 0 5px #6a11cb, 0 0 10px #2575fc;}
        100% {text-shadow: 0 0 20px #ff758c, 0 0 30px #ff7eb3;}
    }
    .container {
        background: rgba(255, 255, 255, 0.2);
        padding: 70px;
        border-radius: 20px;
        box-shadow: 0px 0px 25px rgba(0,0,0,0.4);
        max-width: 750px;
        margin: 30px auto;
        animation: slideIn 1.5s ease;
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
    </style>
""", unsafe_allow_html=True)


st.markdown('<div class="title"> Method Resolution Order (MRO) and Diamond Inheritance</div>', unsafe_allow_html=True)


class A:
    def show(self):
        return "Showing from Class A"

class B(A):
    def show(self):
        return "Showing from Class B"

class C(A):
    def show(self):
        return "Showing from Class C"

class D(B, C):
    pass



st.subheader("Understanding Diamond Inheritance ")
st.write("""
In **Diamond Inheritance**, Class `D` inherits from both `B` and `C`, and both inherit from `A`.
When we call `show()` on object of `D`, Python follows **MRO** to decide which `show()` method to call.
""")

if st.button("Create Object of D and Call show()"):
    d = D()
    result = d.show()
    st.markdown(f'<div class="output">{result}</div>', unsafe_allow_html=True)

if st.button("View MRO Order for D"):
    mro_list = " ➔ ".join(cls.__name__ for cls in D.__mro__)
    st.markdown(f'<div class="output">MRO Order:<br>{mro_list}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
