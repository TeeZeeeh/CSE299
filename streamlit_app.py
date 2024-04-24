import streamlit as st

st.set_page_config(page_title="Echocardiogram Analysis", page_icon="heart", layout="wide")

st.header("Echocardiogram Analysis")

uploaded_files = st.file_uploader(label = "Upload your echocardiogram", type = ["avi"], accept_multiple_files = False)



