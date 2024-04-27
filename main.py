import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Define the directory containing the data
data_dir = os.path.join(script_dir, 'data')

# Load the Data
df_hh_income = pd.read_csv(os.path.join(data_dir, 'Median_Household_Income_2015.csv'), encoding="windows-1252")
df_pct_poverty = pd.read_csv(os.path.join(data_dir, 'Pct_People_Below_Poverty_Level.csv'), encoding="windows-1252")
df_pct_completed_hs = pd.read_csv(os.path.join(data_dir, 'Pct_Over_25_Completed_High_School.csv'), encoding="windows-1252")
df_share_race_city = pd.read_csv(os.path.join(data_dir, 'Share_of_Race_By_City.csv'), encoding="windows-1252")
df_fatalities = pd.read_csv(os.path.join(data_dir, 'Deaths_by_Police_US.csv'), encoding="windows-1252")

# Data Exploration
# Shape of the DataFrames
print("Shape of df_hh_income:", df_hh_income.shape)
print("Shape of df_pct_poverty:", df_pct_poverty.shape)
print("Shape of df_pct_completed_hs:", df_pct_completed_hs.shape)
print("Shape of df_share_race_city:", df_share_race_city.shape)
print("Shape of df_fatalities:", df_fatalities.shape)

# Column names
print("Columns of df_hh_income:", df_hh_income.columns)
print("Columns of df_pct_poverty:", df_pct_poverty.columns)
print("Columns of df_pct_completed_hs:", df_pct_completed_hs.columns)
print("Columns of df_share_race_city:", df_share_race_city.columns)
print("Columns of df_fatalities:", df_fatalities.columns)

# Check for NaN values and duplicates
print("NaN values in df_hh_income:", df_hh_income.isna().sum().sum())
print("NaN values in df_pct_poverty:", df_pct_poverty.isna().sum().sum())
print("NaN values in df_pct_completed_hs:", df_pct_completed_hs.isna().sum().sum())
print("NaN values in df_share_race_city:", df_share_race_city.isna().sum().sum())
print("NaN values in df_fatalities:", df_fatalities.isna().sum().sum())
print("Duplicates in df_hh_income:", df_hh_income.duplicated().sum())
print("Duplicates in df_pct_poverty:", df_pct_poverty.duplicated().sum())
print("Duplicates in df_pct_completed_hs:", df_pct_completed_hs.duplicated().sum())
print("Duplicates in df_share_race_city:", df_share_race_city.duplicated().sum())
print("Duplicates in df_fatalities:", df_fatalities.duplicated().sum())

# Data Cleaning
# No cleaning needed as per the provided information

# Visualization
# Chart the Poverty Rate in each US State
plt.figure(figsize=(12, 6))
sns.barplot(x='City', y='poverty_rate', hue='Geographic Area', data=df_pct_poverty)
plt.title('Poverty Rate by City')
plt.xlabel('City')
plt.ylabel('Poverty Rate')
plt.xticks(rotation=90)
plt.show()

# Chart the High School Graduation Rate by US State
plt.figure(figsize=(12, 6))
sns.barplot(x='City', y='percent_completed_hs', hue='Geographic Area', data=df_pct_completed_hs)
plt.title('High School Graduation Rate by City')
plt.xlabel('City')
plt.ylabel('High School Graduation Rate (%)')
plt.xticks(rotation=90)
plt.show()

# Visualise the Relationship between Poverty Rates and High School Graduation Rates
plt.figure(figsize=(12, 6))
sns.scatterplot(x='poverty_rate', y='percent_completed_hs', data=df_pct_poverty)
plt.title('Relationship between Poverty Rates and High School Graduation Rates')
plt.xlabel('Poverty Rate')
plt.ylabel('High School Graduation Rate (%)')
plt.show()

# Create a Bar Chart with Subsections Showing the Racial Makeup of Each US State
df_share_race_city.set_index('City', inplace=True)
df_share_race_city.plot(kind='bar', stacked=True, figsize=(14, 8))
plt.title('Racial Makeup by City')
plt.xlabel('City')
plt.ylabel('Percentage')
plt.xticks(rotation=45)
plt.legend(title='Race')
plt.show()

# Create Donut Chart by of People Killed by Race
plt.figure(figsize=(8, 8))
df_fatalities['race'].value_counts().plot.pie(autopct='%1.1f%%', startangle=140, colors=sns.color_palette("Set3", len(df_fatalities['race'].unique())))
plt.title('People Killed by Race')
plt.ylabel('')
plt.show()

# Create a Chart Comparing the Total Number of Deaths of Men and Women
plt.figure(figsize=(8, 6))
df_fatalities['gender'].value_counts().plot(kind='bar', color=['blue', 'pink'])
plt.title('Total Number of Deaths of Men and Women')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

# Create a Box Plot Showing the Age and Manner of Death
plt.figure(figsize=(10, 6))
sns.boxplot(x='manner_of_death', y='age', hue='gender', data=df_fatalities)
plt.title('Age and Manner of Death by Gender')
plt.xlabel('Manner of Death')
plt.ylabel('Age')
plt.show()

# Were People Armed?
armed_counts = df_fatalities['armed'].value_counts()
plt.figure(figsize=(10, 6))
armed_counts.plot(kind='bar', color='skyblue')
plt.title('Armed Status of People Killed by Police')
plt.xlabel('Armed Status')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# How Old Were the People Killed?
plt.figure(figsize=(10, 6))
sns.histplot(df_fatalities['age'], kde=True, color='skyblue')
plt.title('Distribution of Ages of People Killed by Police')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Race of People Killed
plt.figure(figsize=(10, 6))
df_fatalities['race'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Race of People Killed by Police')
plt.xlabel('Race')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Mental Illness and Police Killings
mental_illness_percentage = (df_fatalities['signs_of_mental_illness'].sum() / len(df_fatalities)) * 100
print("Percentage of people killed by police with signs of mental illness: {:.2f}%".format(mental_illness_percentage))

# In Which Cities Do the Most Police Killings Take Place?
top_10_cities = df_fatalities['city'].value_counts().head(10)
plt.figure(figsize=(10, 6))
top_10_cities.plot(kind='bar', color='skyblue')
plt.title('Top 10 Cities with the Most Police Killings')
plt.xlabel('City')
plt.ylabel('Number of Police Killings')
plt.xticks(rotation=45)
plt.show()

# Rate of Death by Race in Top 10 Cities
top_10_cities_fatalities = df_fatalities[df_fatalities['city'].isin(top_10_cities.index)]
rate_of_death_by_race = top_10_cities_fatalities['race'].value_counts(normalize=True) * 100
print("Rate of Death by Race in Top 10 Cities:")
print(rate_of_death_by_race)

# Create a Choropleth Map of Police Killings by US State
fatalities_by_state = df_fatalities['state'].value_counts().reset_index()
fatalities_by_state.columns = ['State', 'Fatalities']
fig = px.choropleth(fatalities_by_state, locations='State', locationmode='USA-states', color='Fatalities',
                    color_continuous_scale='Viridis', scope='usa', title='Police Killings by US State')
fig.show()

# Number of Police Killings Over Time
df_fatalities['date'] = pd.to_datetime(df_fatalities['date'])
df_fatalities['year'] = df_fatalities['date'].dt.year
police_killings_over_time = df_fatalities['year'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
sns.lineplot(x=police_killings_over_time.index, y=police_killings_over_time.values, marker='o')
plt.title('Number of Police Killings Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Police Killings')
plt.xticks(police_killings_over_time.index)
plt.show()
