
import streamlit as st

# This hides the top-right menu and footer
st.set_page_config(
    page_title="My App",        # name on browser tab
    page_icon="📊",              # icon on browser tab
    layout="wide"               # full width layout
)

# Hide hamburger menu & footer
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# Your actual app code below
st.text("Hello Akshay")
