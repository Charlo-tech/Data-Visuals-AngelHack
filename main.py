import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Data Visio", page_icon=":bar_chart:", layout="wide")

df = pd.read_csv(
                 io="data.csv",
                 engine="openpyxl",
                 sheet_name="Sheet1",
                 skiprows=1,
                 usecols="A:G",
                 nrows=100,)
io=st.sidebar.selectbox("Select the type of graph",["Bar Chart","Line Chart","Scatter Plot","Pie Chart"])


st.dataframe(df)