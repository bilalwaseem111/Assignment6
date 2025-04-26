import streamlit as st # type: ignore


st.markdown("""
    <style>
    body {
        background: linear-gradient(to bottom right, #141e30, #243b55);
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 3.8em;
        text-align: center;
        font-weight: bold;
        color: Brown;
        margin-top: 30px;
        animation: glow 1s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from { text-shadow: 12 2 10px #33ccff, 0 0 20px #33ccff; }
        to { text-shadow: 0 0 20px #ff66cc, 0 0 30px #ff66cc; }
    }
    .box {
        background: rgba(255, 255, 255, 0.07);
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 0 25px rgba(255,255,255,0.15);
        width: 90%;
        max-width: 600px;
        margin: 30px auto;
        animation: slideIn 1.2s ease-in-out;
    }
    @keyframes slideIn {
        from {opacity: 0; transform: translateY(50px);}
        to {opacity: 1; transform: translateY(0);}
    }
    .output {
        margin-top: 20px;
        padding: 20px;
        border-radius: 10px;
        background-color: rgba(0, 0, 0, 0.5);
        color: Blue;
        font-size: 1.3em;
        text-align: center;
        animation: fadeIn 1s ease-in-out;
    }
    .footer {
        text-align: center;
        color: black;
        font-weight: bold;
        margin-top: 50px;
        font-size: 18px;
        animation: fadeIn 2s ease-in;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown('<div class="title"> Meet Your Dog!</div>', unsafe_allow_html=True)


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says: Woof Woof! 🐾"

    def get_details(self):
        return f"Name: {self.name} | Breed: {self.breed}"


name = st.text_input("Enter Dog's Name")
breed = st.selectbox("Select Dog's Breed", ["Labrador", "Golden Retriever", "German Shepherd", "Poodle", "Bulldog", "Mixed Breed"])
st.markdown('</div>', unsafe_allow_html=True)


if st.button("Show Dog Info"):
    if name.strip() == "":
        st.warning("Please enter your dog's name.")
    else:
        my_dog = Dog(name, breed)
        bark_message = my_dog.bark()
        details = my_dog.get_details()
        st.markdown(f'<div class="output">{details}<br>{bark_message}</div>', unsafe_allow_html=True)


st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
