import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import numpy as np

# Set page config
st.set_page_config(
    page_title="CORD-19 Data Explorer",
    page_icon=":microscope:",
    layout="wide"
)

# Load the data
@st.cache_data
def load_data():
    df = pd.read_csv('data/metadata.csv')
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract_word_count'] = df['abstract'].apply(lambda x: len(str(x).split()) if pd.notnull(x) else 0)
    df = df.dropna(subset=['title', 'abstract'])
    df = df[df['year'].between(2019, 2022)]
    return df

df = load_data()

# Title and description
st.title("CORD-19 Data Explorer")
st.write("""
This interactive dashboard explores the CORD-19 dataset, which contains metadata about COVID-19 research papers.
Use the filters below to explore the data.
""")

# Sidebar filters
st.sidebar.header("Filters")
year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=int(df['year'].min()),
    max_value=int(df['year'].max()),
    value=(2020, 2021)
)

min_abstract_length = st.sidebar.slider(
    "Minimum Abstract Length (words)",
    min_value=0,
    max_value=500,
    value=50
)

# Filter data based on selections
filtered_df = df[
    (df['year'].between(year_range[0], year_range[1])) &
    (df['abstract_word_count'] >= min_abstract_length)
]

# Display basic stats
col1, col2, col3 = st.columns(3)
col1.metric("Total Papers", len(filtered_df))
col2.metric("Years Covered", f"{year_range[0]} - {year_range[1]}")
col3.metric("Avg. Abstract Length", f"{filtered_df['abstract_word_count'].mean():.1f} words")

# Tabs for different visualizations
tab1, tab2, tab3, tab4 = st.tabs([
    "Publications Over Time", 
    "Top Journals", 
    "Title Word Cloud", 
    "Data Sample"
])

with tab1:
    st.header("Publications Over Time")
    year_counts = filtered_df['year'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    year_counts.plot(kind='bar', ax=ax)
    ax.set_title('Number of Publications by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Count')
    plt.xticks(rotation=45)
    st.pyplot(fig)

with tab2:
    st.header("Top Journals")
    top_journals = filtered_df['journal'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    top_journals.plot(kind='barh', ax=ax)
    ax.set_title('Top 10 Journals by Publication Count')
    ax.set_xlabel('Count')
    ax.set_ylabel('Journal')
    st.pyplot(fig)

with tab3:
    st.header("Word Cloud of Paper Titles")
    title_text = ' '.join(filtered_df['title'].dropna().astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(title_text)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title('Word Cloud of Paper Titles')
    st.pyplot(fig)

with tab4:
    st.header("Sample of Data")
    st.dataframe(filtered_df[['title', 'journal', 'year', 'abstract_word_count']].head(10))

# Additional information
st.sidebar.info("""
The CORD-19 dataset is provided by the Allen Institute for AI.
It contains metadata about COVID-19 and coronavirus-related research papers.
""")