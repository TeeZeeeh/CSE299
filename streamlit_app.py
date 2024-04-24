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
    st.write("Predicting the Ejection Fraction...")
    time.sleep(1)
    st.write("Assessing Cardiomyopathy...")
    time.sleep(2)

st.success('Done!', icon="✅")

filelist = pd.read_csv("FileList.csv")
st.table(filelist)

st.markdone("The Ejection Fraction is: ")

st.button('Rerun')

