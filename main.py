""" import pandas as pd
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


st.dataframe(df) """

import streamlit as st
import pandas as pd
import plotly.express as px

# Load the university rankings data from a CSV file
data = pd.read_csv("2011_rankings.csv")

# Set the page title
st.title("University Rankings")

# Create a sidebar with options for different chart types
chart_type = st.sidebar.selectbox("Select chart type", ["Bar chart", "Line graph", "Pie chart"])

# Display the data in the selected chart type
if chart_type == "Bar chart":
    st.bar_chart(data)
elif chart_type == "Line graph":
    st.line_chart(data)
elif chart_type == "Pie chart":
    st.plotly_chart(px.pie(data, values='rank', names='name'))

# Display the data table
st.write("Data table", data)
