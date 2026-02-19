import pandas as pd
import numpy as np

# Part 1: Data Analysis with Pandas

# Load the dataset
# Dataset: Netflix Movies and TV Shows
# Source: https://www.kaggle.com/datasets/shivamb/netflix-shows
# Download link: https://raw.githubusercontent.com/datasciencedojo/datasets/master/netflix_titles.csv

df = pd.read_csv('netflix_titles.csv')

print("Dataset loaded successfully!")
print(f"Shape: {df.shape}")
print("\nFirst few rows:")
print(df.head())

print("\n" + "="*80)
print("DATA ANALYSIS TASKS")
print("="*80)

# Task 1: Calculate the mean and median of release years
print("\n1. DESCRIPTIVE STATISTICS - Release Year")
print("-" * 50)
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
mean_year = df['release_year'].mean()
median_year = df['release_year'].median()
print(f"Mean release year: {mean_year:.2f}")
print(f"Median release year: {median_year:.0f}")
print(f"Earliest release: {df['release_year'].min():.0f}")
print(f"Latest release: {df['release_year'].max():.0f}")

# Task 2: Filter data for recent content (after 2020)
print("\n2. FILTERING - Content Released After 2020")
print("-" * 50)
recent_content = df[df['release_year'] > 2020]
print(f"Total content after 2020: {len(recent_content)}")
print(f"Movies: {len(recent_content[recent_content['type'] == 'Movie'])}")
print(f"TV Shows: {len(recent_content[recent_content['type'] == 'TV Show'])}")

# Task 3: Group by country and calculate average content per type
print("\n3. AGGREGATION - Content by Country and Type")
print("-" * 50)
# Clean country data (take first country if multiple listed)
df['primary_country'] = df['country'].fillna('Unknown').str.split(',').str[0].str.strip()

country_analysis = df.groupby(['primary_country', 'type']).size().reset_index(name='count')
top_countries = country_analysis.groupby('primary_country')['count'].sum().nlargest(10)

print("\nTop 10 countries by content production:")
for idx, (country, count) in enumerate(top_countries.items(), 1):
    print(f"{idx}. {country}: {count} titles")

# Additional analysis: Content by rating
print("\n4. BONUS ANALYSIS - Content Distribution by Rating")
print("-" * 50)
rating_dist = df['rating'].value_counts().head(10)
print(rating_dist)

# Save results to CSV files
print("\n" + "="*80)
print("SAVING RESULTS")
print("="*80)

# Save filtered recent content
recent_content.to_csv('netflix_recent_content.csv', index=False)
print("\n✓ Saved: netflix_recent_content.csv")

# Save country analysis
country_analysis.to_csv('netflix_country_analysis.csv', index=False)
print("✓ Saved: netflix_country_analysis.csv")

# Save rating distribution
rating_dist.to_frame('count').to_csv('netflix_rating_distribution.csv')
print("✓ Saved: netflix_rating_distribution.csv")

# Create a summary statistics file
summary_stats = pd.DataFrame({
    'Metric': ['Total Titles', 'Movies', 'TV Shows', 'Mean Release Year', 
               'Median Release Year', 'Countries Represented', 'Recent Titles (>2020)'],
    'Value': [
        len(df),
        len(df[df['type'] == 'Movie']),
        len(df[df['type'] == 'TV Show']),
        f"{mean_year:.2f}",
        f"{median_year:.0f}",
        df['primary_country'].nunique(),
        len(recent_content)
    ]
})
summary_stats.to_csv('netflix_summary_statistics.csv', index=False)
print("✓ Saved: netflix_summary_statistics.csv")

print("\nAnalysis complete! All results saved.")




#------------------------part2----------------------------------




import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title="Netflix Data Analysis",
    page_icon="🎬",
    layout="wide"
)

# Title and description
st.title("🎬 Netflix Movies and TV Shows Dashboard")
st.markdown("""
This interactive dashboard analyzes Netflix content data.
Use the sidebar to filter the data and explore different visualizations.
""")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('netflix_titles.csv')
    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['primary_country'] = df['country'].fillna('Unknown').str.split(',').str[0].str.strip()
    return df

try:
    df = load_data()
    
    # Sidebar filters
    st.sidebar.header("🔍 Filter Options")
    
    # Content type filter
    content_types = ['All'] + sorted(df['type'].dropna().unique().tolist())
    selected_type = st.sidebar.selectbox("Select Content Type", content_types)
    
    # Year range filter
    min_year = int(df['release_year'].min())
    max_year = int(df['release_year'].max())
    year_range = st.sidebar.slider(
        "Select Release Year Range",
        min_value=min_year,
        max_value=max_year,
        value=(2015, max_year)
    )
    
    # Country filter
    top_countries = df['primary_country'].value_counts().head(20).index.tolist()
    selected_countries = st.sidebar.multiselect(
        "Select Countries (optional)",
        options=top_countries,
        default=[]
    )
    
    # Rating filter
    ratings = ['All'] + sorted(df['rating'].dropna().unique().tolist())
    selected_rating = st.sidebar.selectbox("Select Rating", ratings)
    
    # Apply filters
    filtered_df = df.copy()
    
    if selected_type != 'All':
        filtered_df = filtered_df[filtered_df['type'] == selected_type]
    
    filtered_df = filtered_df[
        (filtered_df['release_year'] >= year_range[0]) & 
        (filtered_df['release_year'] <= year_range[1])
    ]
    
    if selected_countries:
        filtered_df = filtered_df[filtered_df['primary_country'].isin(selected_countries)]
    
    if selected_rating != 'All':
        filtered_df = filtered_df[filtered_df['rating'] == selected_rating]
    
    # Display metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Titles", len(filtered_df))
    with col2:
        movies = len(filtered_df[filtered_df['type'] == 'Movie'])
        st.metric("Movies", movies)
    with col3:
        tv_shows = len(filtered_df[filtered_df['type'] == 'TV Show'])
        st.metric("TV Shows", tv_shows)
    with col4:
        countries = filtered_df['primary_country'].nunique()
        st.metric("Countries", countries)
    
    # Tabs for different views
    tab1, tab2, tab3 = st.tabs(["📊 Visualizations", "📋 Data Table", "📈 Statistics"])
    
    with tab1:
        st.subheader("Data Visualizations")
        
        # Two columns for charts
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Content Released Per Year")
            yearly_counts = filtered_df.groupby('release_year').size().reset_index(name='count')
            
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            ax1.plot(yearly_counts['release_year'], yearly_counts['count'], 
                    marker='o', linewidth=2, markersize=6, color='#E50914')
            ax1.set_xlabel('Release Year', fontsize=12)
            ax1.set_ylabel('Number of Titles', fontsize=12)
            ax1.grid(True, alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig1)
        
        with col2:
            st.markdown("#### Content by Type")
            type_counts = filtered_df['type'].value_counts()
            
            fig2, ax2 = plt.subplots(figsize=(10, 6))
            colors = ['#E50914', '#B20710']
            ax2.bar(type_counts.index, type_counts.values, color=colors)
            ax2.set_xlabel('Content Type', fontsize=12)
            ax2.set_ylabel('Number of Titles', fontsize=12)
            ax2.grid(True, alpha=0.3, axis='y')
            plt.tight_layout()
            st.pyplot(fig2)
        
        # Full width chart
        st.markdown("#### Top 15 Countries by Content Production")
        country_counts = filtered_df['primary_country'].value_counts().head(15)
        
        fig3, ax3 = plt.subplots(figsize=(12, 6))
        ax3.barh(country_counts.index[::-1], country_counts.values[::-1], color='#E50914')
        ax3.set_xlabel('Number of Titles', fontsize=12)
        ax3.set_ylabel('Country', fontsize=12)
        ax3.grid(True, alpha=0.3, axis='x')
        plt.tight_layout()
        st.pyplot(fig3)
        
        # Rating distribution
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Rating Distribution")
            rating_counts = filtered_df['rating'].value_counts().head(10)
            
            fig4, ax4 = plt.subplots(figsize=(10, 6))
            ax4.pie(rating_counts.values, labels=rating_counts.index, autopct='%1.1f%%',
                   startangle=90, colors=sns.color_palette('Reds_r', len(rating_counts)))
            ax4.axis('equal')
            plt.tight_layout()
            st.pyplot(fig4)
        
        with col2:
            st.markdown("#### Content Added Over Time")
            if filtered_df['date_added'].notna().any():
                monthly_added = filtered_df.dropna(subset=['date_added'])
                monthly_added = monthly_added.set_index('date_added').resample('M').size()
                
                fig5, ax5 = plt.subplots(figsize=(10, 6))
                ax5.plot(monthly_added.index, monthly_added.values, 
                        color='#E50914', linewidth=2)
                ax5.set_xlabel('Date Added', fontsize=12)
                ax5.set_ylabel('Number of Titles', fontsize=12)
                ax5.grid(True, alpha=0.3)
                plt.xticks(rotation=45)
                plt.tight_layout()
                st.pyplot(fig5)
    
    with tab2:
        st.subheader("Filtered Data Table")
        st.markdown(f"Showing {len(filtered_df)} of {len(df)} total titles")
        
        # Select columns to display
        display_columns = ['type', 'title', 'director', 'primary_country', 
                          'release_year', 'rating', 'duration']
        available_cols = [col for col in display_columns if col in filtered_df.columns]
        
        st.dataframe(
            filtered_df[available_cols].head(500),
            use_container_width=True,
            height=400
        )
        
        # Download button
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Filtered Data as CSV",
            data=csv,
            file_name="netflix_filtered_data.csv",
            mime="text/csv"
        )
    
    with tab3:
        st.subheader("Statistical Summary")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Release Year Statistics")
            stats_df = pd.DataFrame({
                'Statistic': ['Mean', 'Median', 'Min', 'Max', 'Std Dev'],
                'Value': [
                    f"{filtered_df['release_year'].mean():.2f}",
                    f"{filtered_df['release_year'].median():.0f}",
                    f"{filtered_df['release_year'].min():.0f}",
                    f"{filtered_df['release_year'].max():.0f}",
                    f"{filtered_df['release_year'].std():.2f}"
                ]
            })
            st.dataframe(stats_df, use_container_width=True, hide_index=True)
        
        with col2:
            st.markdown("#### Content Type Distribution")
            type_stats = filtered_df['type'].value_counts().reset_index()
            type_stats.columns = ['Type', 'Count']
            type_stats['Percentage'] = (type_stats['Count'] / len(filtered_df) * 100).round(2)
            st.dataframe(type_stats, use_container_width=True, hide_index=True)
        
        st.markdown("#### Top 10 Genres")
        if 'listed_in' in filtered_df.columns:
            genres = filtered_df['listed_in'].str.split(',', expand=True).stack()
            genres = genres.str.strip().value_counts().head(10).reset_index()
            genres.columns = ['Genre', 'Count']
            st.dataframe(genres, use_container_width=True, hide_index=True)

except FileNotFoundError:
    st.error("""
    ❌ **Error: Dataset not found!**
    
    Please download the Netflix dataset and save it as `netflix_titles.csv` in the same directory as this script.
    
    **Download link:** https://raw.githubusercontent.com/datasciencedojo/datasets/master/netflix_titles.csv
    
    Or download from Kaggle: https://www.kaggle.com/datasets/shivamb/netflix-shows
    """)
except Exception as e:
    st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
**Data Source:** [Netflix Movies and TV Shows Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)  
**Created with:** Streamlit, Pandas, Matplotlib, Seaborn
""")