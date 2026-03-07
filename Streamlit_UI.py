import streamlit as st
import pandas as pa
import numpy as np


def load_data(path):
    data = pa.read_excel(path)
    return data

def choosing_path(Input):
    
    if Input == "Culture data":
        return r"C:\Users\ELOUAN\Desktop\INRS\Culture Follow up\Culture_data.xlsx"
    elif Input == "Media":
        return r"C:\Users\ELOUAN\Desktop\INRS\Culture Follow up\Media.xlsx"
    elif Input == "Task log":
        return r"C:\Users\ELOUAN\Desktop\INRS\Culture Follow up\Daily_log.xlsx"
    else:
        st.warning("Please enter a valid path.")
        return None


## Structure of the page
# Add a selectbox to the sidebar:
def page_Cultures():
    st.title("This is the Culture Follow-up Dashboard !")
    Layout = st.columns([1, 2])
    with Layout[1]:
        tile1 = st.container(border=True,height="stretch")
        tile1.title(":balloon:")
        tile2 = st.container(border=True,height="stretch")
        tile2.title(":balloon:")
    Data_to_display = Layout[0].selectbox(
        'Select the data you want to display',['Culture data','Media'])
    path = choosing_path(Data_to_display)
    Layout[0].write(load_data(path))


pg = st.navigation([r"C:\Users\ELOUAN\Desktop\INRS\Culture Follow up\Cyanobacteria_Culture\Streamlit_UI_page_Daily_log.py",page_Cultures])
pg.run()
