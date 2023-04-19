import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Load the university rankings data from a CSV file
# Load data from CSV files for each year
data_2011 = pd.read_csv("2011_rankings.csv")
data_2012 = pd.read_csv("2012_rankings.csv")
data_2013 = pd.read_csv("2013_rankings.csv")
data_2014 = pd.read_csv("2014_rankings.csv")
data_2015 = pd.read_csv("2015_rankings.csv")
data_2016 = pd.read_csv("2016_rankings.csv")
data_2017 = pd.read_csv("2017_rankings.csv")
data_2018 = pd.read_csv("2018_rankings.csv")
data_2019 = pd.read_csv("2019_rankings.csv")
data_2020 = pd.read_csv("2020_rankings.csv")
data_2021 = pd.read_csv("2021_rankings.csv")
data_2022 = pd.read_csv("2022_rankings.csv")
data_2023 = pd.read_csv("2023_rankings.csv")

# Combine all data into a single dataframe
data_combo = pd.concat([data_2011, data_2012, data_2013, data_2014, data_2015, data_2016, data_2017, data_2018, data_2019, data_2020, data_2021, data_2022, data_2023], axis=0)

# Set the page title
st.title("University Rankings")

# Create a sidebar with options for different chart types and pages
st.sidebar.success("view other pages above")

chart_type = st.sidebar.selectbox("Select chart type", ["Bar chart", "Line graph", "Pie chart"])
Data_table = st.sidebar.checkbox("Show data table", True)
year_rank = st.sidebar.slider("Select year", 2011, 2023, 2011)

# Display the data in the selected chart type
if chart_type == "Bar chart" and year_rank == "2011":
    # Create bar chart
    fig, ax = plt.subplots()
    ax.bar(data_2011["name"], data_2011["scores_overall"])

    # Set chart title and axes labels
    ax.set_title("Overall rankings by university")
    ax.set_xlabel("name")
    ax.set_ylabel("scores_overall")

    st.pyplot(fig)
elif chart_type == "Bar chart" and year_rank == "2012":
    # Create bar chart
    fig, ax = plt.subplots()
    ax.bar(data_2012["name"], data_2012["scores_overall"])

    # Set chart title and axes labels
    ax.set_title("Overall rankings by university")
    ax.set_xlabel("name")
    ax.set_ylabel("scores_overall")

    st.pyplot(fig)
elif chart_type == "Line graph":
    st.line_chart(data_combo, )
elif chart_type == "Pie chart":
    st.plotly_chart(px.pie(data_combo, values='scores_overall', names='name'))

# Display the data table
st.write("Data table", data_combo)
