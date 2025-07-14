import streamlit as st
import pandas as pd
import numpy as np

## Title of the app
st.title("Streamlit App")

## Display a simple text
st.write("This is a simple Streamlit app.")

## Create a DataFrame
data = {
    'Column 1': [1, 2, 3, 4, 5],
    'Column 2': ['A', 'B', 'C', 'D', 'E'],
    'Column 3': [10.5, 20.5, 30.5, 40.5, 50.5]
}
df = pd.DataFrame(data) 
## Display the DataFrame
st.write("Here is a sample DataFrame:")
st.dataframe(df)

## Create a line chart
st.write("Line Chart:")
st.line_chart(df['Column 1'])