import streamlit as st

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #FF1493, #8B008B);
        font-family: 'Arial', sans-serif;
    }
    .title {
        font-size: 3em;
        text-align: center;
        font-weight: bold;
        color: brown;
        margin-top: 20px;
        animation: colorChange 4s infinite alternate;
    }
    @keyframes colorChange {
        0% {text-shadow: 0 0 10px #ffffff, 0 0 20px #FF1493;}
        100% {text-shadow: 0 0 10px #FFD700, 0 0 20px #8B008B;}
    }
    .container {
        background: rgba(0, 0, 0, 0.7);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 0px 25px rgba(0,0,0,0.5);
        max-width: 800px;
        margin: 30px auto;
        animation: slideIn 1.5s ease-in-out;
    }
    @keyframes slideIn {
        from {opacity: 0; transform: translateY(-50px);}
        to {opacity: 1; transform: translateY(0);}
    }
    .output {
        margin-top: 20px;
        padding: 20px;
        border-radius: 15px;
     
        color: red;
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
    @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Property Decorators: @property, @setter, @deleter</div>', unsafe_allow_html=True)

class Product:
    def __init__(self, price):
        self._price = float(price)  # Ensure price is always a float

    # @property - Getter
    @property
    def price(self):
        return self._price

    # @price.setter - Setter
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = float(value)  # Ensure price is always a float

    # @price.deleter - Deleter
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price


st.subheader("Property Decorators in Action ")
st.write("""
In this example, we have used **property decorators** in the `Product` class to manage the price of the product. 
- The `@property` decorator allows us to get the value of the price.
- The `@price.setter` decorator allows us to set the price, with validation to ensure it is not negative.
- The `@price.deleter` decorator enables deleting the price attribute.
""")

product = Product(price=100)  # Initial price

# Buttons for interaction
if st.button("Get Product Price"):
    st.markdown(f'<div class="output">Price: ${product.price}</div>', unsafe_allow_html=True)

# Set new price
new_price = st.number_input("Enter a new price:", min_value=0.0, value=product.price, format="%.2f")

if st.button("Update Price"):
    try:
        product.price = new_price  # Set the new price
        st.markdown(f'<div class="output">Price updated to: ${product.price}</div>', unsafe_allow_html=True)
    except ValueError as e:
        st.error(str(e))

# Delete price
if st.button("Delete Price"):
    del product.price  # Delete the price
    st.markdown('<div class="output">Price deleted successfully!</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
