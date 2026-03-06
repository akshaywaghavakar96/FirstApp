import streamlit as st

st.set_page_config(page_title="My App", layout="wide")

hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Hides mobile bottom banner */
    .viewerBadge_container__1QSob {display: none;}
    .viewerBadge_link__1S137 {display: none;}
    [data-testid="stToolbar"] {display: none;}
    .stDeployButton {display: none;}
    #stDecoration {display: none;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

st.text("Hello Akshay")