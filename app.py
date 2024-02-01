# importing necessary libraries
import streamlit as st 
import pandas as pd 
import plotly.express as px

# reading the data to a pandas dataframe
vehicle_df = pd.read_csv('/home/john/Software_dev_tools_project-1/vehicles_us.csv', sep=',')

# Fixing, renaming, and changing colummn headers and values
# renaming columns
vehicle_df = vehicle_df.rename(columns={'price' : 'price_in_usd', 'model' : 'model_name', 'odometer' : 'odometer_in_miles', 'type' : 'body_type'})

#Filling in missing values for is_4wd column
vehicle_df['is_4wd'] = vehicle_df['is_4wd'].fillna(0)

# changing data types
vehicle_df['price_in_usd'] = vehicle_df['price_in_usd'].astype('float64', errors='ignore')
vehicle_df['model_year'] = vehicle_df['model_year'].astype('int64', errors='ignore')
vehicle_df['cylinders'] = vehicle_df['cylinders'].astype('int64', errors='ignore')
vehicle_df['is_4wd'] = vehicle_df['is_4wd'].astype('int64', errors='ignore')


st.header("AVG Price per Model Year")

avg_price_per_year = vehicle_df.groupby('model_year')['price_in_usd'].mean().reset_index()

avg_price_per_year_scatter = px.scatter(avg_price_per_year, 
                                        x='model_year', 
                                        y='price_in_usd', 
                                        title='Avg Price per Model Year', 
                                        labels={'model_year' : 'model year', 'price_in_usd' : 'price (USD)'}
                                        )
st.write(avg_price_per_year_scatter)

st.header("Models available per year")

models_per_year = vehicle_df['model_year'].value_counts().sort_values().reset_index()
models_per_year_hist = px.histogram(models_per_year, nbins=25, x='model_year', y='count', title="Models Available per Year", labels={'model_year' : 'model year'})

st.write(models_per_year_hist)

all_models = vehicle_df.groupby('body_type')['body_type'].value_counts().reset_index()
is_4wd = vehicle_df[vehicle_df['is_4wd'] == 1].groupby('body_type')['body_type'].value_counts().reset_index()

all_models = all_models[all_models['body_type'] != 'bus']

all_models_bar = px.bar(all_models, x='body_type', y='count', range_y=[0, 12000])
is_4wd_bar = px.bar(is_4wd, x='body_type', y='count', range_y=[0, 12000])

st.header('Body types with and w/o 4wd')

show_4wd = st.checkbox('Models with 4wd')

if show_4wd:
    st.write(is_4wd_bar)
else:
    st.write(all_models_bar)

