import streamlit as st
import pandas as pd

# Function to preprocess the data based on user selections
def preprocess_data(data, selected_columns, preprocessing_method):
    if preprocessing_method == "Drop":
        data = data.dropna(subset=selected_columns)
    elif preprocessing_method == "Imputation":
        for column in selected_columns:
            if data[column].dtype == 'object':
                data[column].fillna(data[column].mode()[0], inplace=True)
            else:
                if len(data[column].unique()) > len(data) * 0.1:
                    data[column].fillna(data[column].mean(), inplace=True)
                else:
                    data[column].fillna(data[column].mode()[0], inplace=True)
    return data

st.title("Clustering Peserta Didik Sekolah Cendekia Harapan")

uploaded_file = st.file_uploader("Choose file CSV", type=["csv"])

if uploaded_file is not None:
    st.write("Uploaded Files:")
    st.write(uploaded_file.name)
    
    data = pd.read_csv(uploaded_file)
    
    st.write("Input File:")
    st.write(data)
    
    st.sidebar.header("Data Preprocessing")
    
    # Allow users to select columns to be clustered
    selected_columns = st.sidebar.multiselect("Select columns to be clustered", data.columns)
    
    # Allow users to select preprocessing method
    preprocessing_method = st.sidebar.radio("Select preprocessing method", ("Drop", "Imputation"))
    
    if preprocessing_method == "Drop":
        preprocessed_data = preprocess_data(data.copy(), selected_columns, preprocessing_method)
        st.write("Preprocessed Data (Dropped Null Values):")
        st.write(preprocessed_data)
    
    elif preprocessing_method == "Imputation":
        preprocessed_data = preprocess_data(data.copy(), selected_columns, preprocessing_method)
        st.write("Preprocessed Data (Imputed with Mode for Objects, Mean/Mode for Numerics):")
        st.write(preprocessed_data)
