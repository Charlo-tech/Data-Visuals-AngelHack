import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Load the university rankings data from a CSV file
data = pd.read_csv("2011_rankings.csv")

# Set the page title
st.title("University Rankings")

# Create a sidebar with options for different chart types
chart_type = st.sidebar.selectbox("Select chart type", ["Bar chart", "Line graph", "Pie chart"])
Data_table = st.sidebar.checkbox("Show data table", True)
year_rank = st.sidebar.slider("Select year", 2011, 2023, 2011)

# Display the data in the selected chart type
if chart_type == "Bar chart":
    # Create bar chart
    fig, ax = plt.subplots()
    ax.bar(data["name"], data["scores_overall"])

    # Set chart title and axes labels
    ax.set_title("Overall rankings by university")
    ax.set_xlabel("X Label")
    ax.set_ylabel("Y Label")
elif chart_type == "Line graph":
    st.line_chart(data, )
elif chart_type == "Pie chart":
    st.plotly_chart(px.pie(data, values='scores_overall', names='name'))

# Display the data table
st.write("Data table", data)
