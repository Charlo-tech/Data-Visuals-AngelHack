import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv("2023_rankings.csv")
    return data

df = load_data()

counts = df["closed"].value_counts()

# Filter only false values
counts = counts[counts.index == False]

# Create pie chart
fig = px.pie(counts, values=counts, names=counts.index,
             title="Open Universities pie chart",
             color_discrete_sequence=px.colors.qualitative.Pastel1,
             template="seaborn")

fig.update_traces(textposition="inside", textinfo="percent+label")

# Create table
table = pd.DataFrame({
    "closed": counts.index,
    "Count of False Values": counts.values
})

st.plotly_chart(fig)
st.write(table)
# Distribution of universities by country 2023

@st.cache_data
def load_data():
    data = pd.read_csv("2023_rankings.csv")
    return data

df = load_data()

# Compute counts by location
counts = df.groupby("location").size().reset_index(name="Count")

# Create pie chart
fig = px.pie(counts, values="Count", names="location", 
             title="University distribution by location",
             hover_data=["Count"], hole=0.3,
             color_discrete_sequence=px.colors.qualitative.Pastel1,
             template="seaborn")

fig.update_traces(textinfo="percent+label", pull=[0.1, 0, 0, 0], 
                  marker=dict(line=dict(color="#000000", width=0.5)))

# Create bar chart
fig = px.bar(counts, x="location", y="Count",
             title="University distribution by location Bar chart",
             hover_data=["Count"],
             color_discrete_sequence=px.colors.qualitative.Pastel1,
             template="seaborn")

fig.update_traces(marker_line_width=1.5, marker_line_color="black")

# Create table
table = pd.DataFrame({
    "location": counts["location"],
    "Count": counts["Count"]
})

st.plotly_chart(fig)
st.write(" University distribution by location", table)

df = df[df['subjects_offered'].str.contains('Computer Science')]

# Sort data by rank and select top 10 universities
df = df.sort_values(by='rank_order', ascending=True).head(10)

# Create table
table = df[['rank_order', 'name']].reset_index(drop=True)
table.index += 1
table.columns = ['rank_order', 'name']
st.write(table)

# Create pie chart
fig = px.pie(df, values='rank_order', names='name',
             title='Top 10 Universities to Study Computer Science',
             color_discrete_sequence=px.colors.qualitative.Pastel1,
             template="seaborn")

fig.update_traces(textposition="inside", textinfo="percent+label")

st.plotly_chart(fig)


