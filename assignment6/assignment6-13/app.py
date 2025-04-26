import streamlit as st # type: ignore


st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #4facfe, #00f2fe);
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 2.8em;
        text-align: center;
        font-weight: bold;
        color: Black;
        background-color: light green;    
        margin-top: 20px;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% {text-shadow: 0 0 5px #ff00c8;}
        50% {text-shadow: 0 0 20px #00e1ff;}
        100% {text-shadow: 0 0 5px #ff00c8;}
    }
    .container {
        background: rgba(255, 255, 255, 0.12);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 0px 30px rgba(255,255,255,0.3);
        max-width: 650px;
        margin: 30px auto;
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(-30px);}
        to {opacity: 1; transform: translateY(0);}
    }
    .output {
        margin-top: 25px;
        padding: 20px;
        border-radius: 15px;
        background-color: rgba(0, 0, 0, 0.6);
        color: grey;
        font-size: 1.4em;
        text-align: center;
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


st.markdown('<div class="title"> Car and Engine Composition</div>', unsafe_allow_html=True)


class Engine:
    def __init__(self, horsepower, engine_type):
        self.horsepower = horsepower
        self.engine_type = engine_type

    def start_engine(self):
        return f"Engine ({self.engine_type}, {self.horsepower} HP) has started."

class Car:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine

    def car_details(self):
        return f"{self.brand} {self.model} with {self.engine.horsepower} HP {self.engine.engine_type} engine."

    def start(self):
        return self.engine.start_engine()




st.subheader("Create Your Car ")
brand = st.text_input("Enter Car Brand:", "Toyota")
model = st.text_input("Enter Car Model:", "Supra")
engine_hp = st.number_input("Enter Engine Horsepower:", min_value=50, max_value=1500, value=300)
engine_type = st.selectbox("Select Engine Type:", ["V6", "V8", "Electric", "Hybrid", "Turbocharged"])

st.markdown('</div>', unsafe_allow_html=True)


if st.button("Create Car"):
    engine = Engine(engine_hp, engine_type)
    car = Car(brand, model, engine)

    st.markdown(f'<div class="output">{car.car_details()}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="output">{car.start()}</div>', unsafe_allow_html=True)


st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
