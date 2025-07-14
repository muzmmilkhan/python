import streamlit as st
import pandas as pd
import numpy as np

# Set the title of the Streamlit app
st.title("Text and Data Widgets")

# Text input widget
text_input = st.text_input("Enter some text:")
if text_input:
    st.write(f"You entered: {text_input}")

# Age slider widget
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is: {age}")

# Selectbox widget for favorite color
colors = ["Red", "Green", "Blue", "Yellow"]
favorite_color = st.selectbox("Select your favorite color:", colors)
st.write(f"Your favorite color is: {favorite_color}")

# DataFrame widget
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
df.to_csv("sample_data.csv", index=False)
st.write("Here is a sample DataFrame:")
st.dataframe(df)

# Upload file widget
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df_uploaded = pd.read_csv(uploaded_file)
    st.write("Uploaded DataFrame:")
    st.dataframe(df_uploaded)