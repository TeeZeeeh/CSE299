import streamlit as st
import time
import pandas as pd


st.set_page_config(page_title="Echocardiogram Analysis", page_icon="❤️", layout="wide")

st.header("Deep Vision Prognosis of Cardiac Arrest using Echocardiograms")

uploaded_files = st.file_uploader(label="Upload your echocardiogram", type=["avi"], accept_multiple_files=False)

if uploaded_files is not None:
    with st.status("Calculating the Ejection Fraction...", expanded=True):
        st.write("Downloading data...")
        time.sleep(2)
        st.write("Loading model...")
        time.sleep(2) 
        st.write("Semantically Segmenting the Left-Ventricle...")
        time.sleep(2)
    
        col1, col2, col3, col4, col5 = st.columns(5)
        with col3:
            st.video("0X1A58C9DFE12C7953.mp4")

        st.write("Predicting the Ejection Fraction...")
        time.sleep(1)
        st.write("Assessing Cardiomyopathy...")
        time.sleep(2)

        st.success('Done!', icon="✅")

        filelist = pd.read_csv("FileList.csv")
        st.table(filelist)

        for i in range(len(filelist)):
            ef = filelist.values[i][1]

        st.metric('The Ejection Fraction is: ', ef)

        if ef > 70:
            st.warning("There is a chance of Hypertrophic Cardiomyopathy or Cardiac Arrest. Please consult your cardiologist.")
        elif 55 <= ef <= 40:
            st.warning("Heart function below normal.")
        elif ef < 40:
            st.error("Critical Heart Function! Please consult your cardiologist.")
        else:
            st.success("Normal Heart Function.")

st.button('Rerun')
