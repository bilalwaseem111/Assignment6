import streamlit as st # type: ignore


st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #bdc3c7, #2c3e50);
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 3.7em;
        text-align: center;
        font-weight: bold;
        color: light blue;
        margin-top: 30px;
        animation: glow 2s infinite alternate;
    }
    @keyframes glow {
        from { text-shadow: 0 0 10px #00ffff; }
        to { text-shadow: 0 0 20px #ff66ff; }
    }
    .box {
        background-color: rgba(255,255,255,0.1);
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 0 30px rgba(255,255,255,0.15);
        width: 90%;
        max-width: 600px;
        margin: 30px auto;
        animation: dropFade 1s ease-in-out;
    }
    @keyframes dropFade {
        from {opacity: 0; transform: translateY(-40px);}
        to {opacity: 1; transform: translateY(0);}
    }
    .output {
        margin-top: 25px;
        padding: 25px;
        border-radius: 12px;
        background-color: rgba(255,255,255,0.08);
        color: grey;
        font-size: 1.3em;
        text-align: center;
        animation: fadeIn 1.2s ease-in-out;
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


st.markdown('<div class="title"> Temperature Converter with Static Method</div>', unsafe_allow_html=True)


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return round((c * 9/5) + 32, 2)



celsius = st.number_input("Enter Temperature in Celsius", value=0.0, step=0.1)
st.markdown('</div>', unsafe_allow_html=True)

if st.button("Convert to Fahrenheit"):
    fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
    st.markdown(f'<div class="output">{celsius}°C is equal to {fahrenheit}°F</div>', unsafe_allow_html=True)


st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
