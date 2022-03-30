import streamlit as st

st.title("Cloud run sample app")

name = st.text_input("Your name?")

st.write(f"Hello, {name or 'world'}!")