import streamlit as st

st.set_page_config(page_title="Echocardiogram Analysis", page_icon="heart", layout="wide")

st.header("Deep Vision Prognosis of Cardiac Arrest using Echocardiograms")

uploaded_files = st.file_uploader(label="Upload your echocardiogram", type=["avi"], accept_multiple_files=False)

display_file = st.video(uploaded_files, format="video/avi", start_time=0, subtitles=None, end_time=None, loop=False)



