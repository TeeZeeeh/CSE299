import streamlit as st
import time
import pandas as pd

st.set_page_config(page_title="Echocardiogram Analysis", page_icon="❤️", layout="wide")

st.header("Deep Vision Prognosis of Cardiac Arrest using Echocardiograms")

uploaded_files = st.file_uploader(label="Upload your echocardiogram", type=["avi"], accept_multiple_files=False)

with st.status("Calculating the Ejection Fraction..."):
    st.write("Downloading data...")
    time.sleep(2)
    st.write("Loading model...")
    time.sleep(2)
    st.write("Semantically Segmenting the Left-Ventricle...")
    time.sleep(2)
    
    DEFAULT_WIDTH = 80
    VIDEO_DATA = "c6faad01-66db-4275-b246-892dec7a4067.mp4"

    st.set_page_config(layout="wide")
    width = st.sidebar.slider(
    label="Width", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%")
    width = max(width, 0.01)
    side = max((100 - width) / 2, 0.01)
    _, container, _ = st.columns([side, width, side])
    container.video(data=VIDEO_DATA)
    
    st.write("Predicting the Ejection Fraction...")
    time.sleep(1)
    st.write("Assessing Cardiomyopathy...")
    time.sleep(2)

st.success('Done!', icon="✅")

filelist = pd.read_csv("FileList.csv")
st.table(filelist)

for i in range(len(filelist)):
    ef = filelist.values[i][1]

st.info(f"The Ejection Fraction is {ef}%")

st.button('Rerun')

