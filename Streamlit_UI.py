import streamlit as st
import pandas as pa

path = r"C:\Users\ELOUAN\Desktop\INRS\Culture Follow up\Culture_data.xlsx"

def load_data(path):
    data = pa.read_excel(path)
    return data

st.text("Hello, welcome to the Culture Follow-up Dashboard !")
st.text(load_data(path))