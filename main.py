import streamlit as st
import requests

st.title("Calculator using API")

# Input numbers
a = st.number_input("Enter Number A", value=0.0)
b = st.number_input("Enter Number B", value=0.0)

# Buttons for operations
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Add"):
        res = requests.get(f"http://127.0.0.1:8000/add?a={a}&b={b}")
        st.success(f"Result: {res.json().get('result')}")

with col2:
    if st.button("Sub"):
        res = requests.get(f"http://127.0.0.1:8000/sub?a={a}&b={b}")
        st.success(f"Result: {res.json().get('result')}")

with col3:
    if st.button("Mul"):
        res = requests.get(f"http://127.0.0.1:8000/mul?a={a}&b={b}")
        st.success(f"Result: {res.json().get('result')}")

with col4:
    if st.button("Div"):
        res = requests.get(f"http://127.0.0.1:8000/div?a={a}&b={b}")
        data = res.json()
        if "error" in data:
            st.error(data["error"])
        else:
            st.success(f"Result: {data.get('result')}")
