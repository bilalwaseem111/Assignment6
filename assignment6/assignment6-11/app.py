import streamlit as st # type: ignore


st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #1e3c72, #2a5298);
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 3.5em;
        text-align: center;
        font-weight: bold;
        color: green;
        margin-top: 30px;
        animation: glow 2s infinite alternate;
    }
    @keyframes glow {
        from { text-shadow: 0 0 15px #00ffff; }
        to { text-shadow: 0 0 25px #ff66ff; }
    }
    .box {
        background-color: rgba(255,255,255,0.08);
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 0 30px rgba(255,255,255,0.2);
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
        margin-top: 20px;
        padding: 20px;
        border-radius: 12px;
        background-color: rgba(255,255,255,0.07);
        color: grey;
        font-size: 1.2em;
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

st.markdown('<div class="title"> Book Tracker with Class Methods</div>', unsafe_allow_html=True)

class Book:
    total_books = 0
    books = []

    def __init__(self, title, author, genre, year, language):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.language = language
        Book.increment_book_count()
        Book.books.append(self)

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    def get_details(self):
        return f" Title: {self.title}<br> Author: {self.author}<br> Genre: {self.genre}<br>📅 Year: {self.year}<br> Language: {self.language}"

title = st.text_input("Enter Book Title")
author = st.text_input("Enter Author Name")
genre = st.selectbox("Select Genre", ["Fiction", "Non-Fiction", "Mystery", "Science", "Fantasy"])
year = st.number_input("Enter Year of Publication", min_value=1000, max_value=2025, step=1)
language = st.selectbox("Select Language", ["English", "Urdu", "Spanish", "French", "German"])
st.markdown('</div>', unsafe_allow_html=True)


if st.button("Add Book"):
    if title.strip() == "" or author.strip() == "":
        st.warning("Please enter both Title and Author!")
    else:
        new_book = Book(title, author, genre, year, language)
        st.markdown(f'<div class="output">{new_book.get_details()}<br><br>📚 Total Books: {Book.get_total_books()}</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Made by Bilal Waseem</div>', unsafe_allow_html=True)
