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
st.write("The data presented shows that all universities are up and running and none is closed as of 2023")

@st.cache_data
def load_data():
    data = pd.read_csv("2023_rankings.csv")
    return data

df = load_data()

counts = df["unaccredited"].value_counts()

# Filter only false values
counts = counts[counts.index == False]

# Create pie chart
fig = px.pie(counts, values=counts, names=counts.index,
             title="Accredited Universities pie chart",
             color_discrete_sequence=px.colors.qualitative.Pastel1,
             template="seaborn")

fig.update_traces(textposition="inside", textinfo="percent+label")

# Create table
table = pd.DataFrame({
    "unaccredited": counts.index,
    "Count of False Values": counts.values
})

st.plotly_chart(fig)
st.write(table)
st.write("The data presented shows that all universities are accredited as of 2023 to offer the various subjects.")
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

@st.cache_data
def load_data():
    data = pd.read_csv("2023_rankings.csv")
    return data

df = load_data()
filtered_data = df[(df["subjects_offered"].str.contains("Computer Science", na=False))]

# Sort data by ranking
top_10 = filtered_data.sort_values(by="rank", ascending=True).head(10)

# Create ranking table
ranking_table = pd.DataFrame({
    "Rank": top_10["rank"],
    "University": top_10["name"],
    "Country": top_10["location"],
    "Score": top_10["scores_overall"]
})

# Create pie chart
location_counts = top_10["location"].value_counts()
fig = px.pie(location_counts, values=location_counts.values, names=location_counts.index,
             title="Top 10 Computer Science Universities by Location",
             color_discrete_sequence=px.colors.qualitative.Pastel1,
             template="seaborn",
             hole=0.6)

fig.update_traces(textinfo="percent+label", marker=dict(line=dict(color="#FFFFFF", width=2)))

# Display ranking table and pie chart
st.write("Top 10 Computer Science Universities in 2023:")
st.write(ranking_table)
st.plotly_chart(fig)

@st.cache_data
def load_data():
    data = pd.read_csv("2023_rankings.csv")
    return data

df = load_data()

# Filter data
filtered_data = df[df["subjects_offered"].str.contains("Language", na=False)]

# Count universities by location
location_counts = filtered_data["location"].value_counts().head(10)

# Create bar chart
fig = px.bar(location_counts, x=location_counts.index, y=location_counts.values,
             title="Top 10 Locations with Universities Offering Languages",
             color_discrete_sequence=px.colors.qualitative.Pastel1,
             template="seaborn")

fig.update_layout(xaxis_title="Location", yaxis_title="Number of Universities")

# Create table
location_table = pd.DataFrame({
    "Location": location_counts.index,
    "Number of Universities": location_counts.values
})

# Display bar chart and table
st.plotly_chart(fig)
st.write(location_table)

@st.cache_data
def load_data():
    data = pd.read_csv("2023_rankings.csv")
    return data

df = load_data()
filtered_data = df[(df["subjects_offered"].str.contains("Civil Engineering", na=False))]

# Sort data by ranking
top_10 = filtered_data.sort_values(by="rank", ascending=True).head(10)

# Create ranking table
ranking_table = pd.DataFrame({
    "Rank": top_10["rank"],
    "University": top_10["name"],
    "Country": top_10["location"],
    "Score": top_10["scores_overall"]
})

# Create pie chart
location_counts = top_10["location"].value_counts()
fig = px.pie(location_counts, values=location_counts.values, names=location_counts.index,
             title="Top 10 Civil Engineering Universities by Location",
             color_discrete_sequence=px.colors.qualitative.Pastel1,
             template="seaborn",
             hole=0.6)

fig.update_traces(textinfo="percent+label", marker=dict(line=dict(color="#FFFFFF", width=2)))

# Display ranking table and pie chart
st.write("Top 10 Civil Engineering Universities in 2023:")
st.write(ranking_table)
st.plotly_chart(fig)