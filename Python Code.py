import pandas as pd
import numpy as np
from datetime import datetime
from fuzzywuzzy import fuzz, process
import logging
import os
from google.colab import files

# Read File Content
print("Please Upload a XLSX File")
uploaded = files.upload()
xlsx_file = list(uploaded.keys())[0]
df = pd.read_excel(xlsx_file)

#Remove Null Rows.
def remove_null_rows(df):
    df_cleaned = df.dropna()
    print(remove_null_rows)

#Split Product column into Car Make & Car Model.
def split_product_column(df):
    df[['Car Make', 'Car Model']] = df['Product'].str.split(' ', 1, expand=True)
    return df
    print(split_product_column)

#Fix Date column - Convert DD/MM/YYYY to be read as date instead of text.
def fix_date_column(df):
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')
    return df
    print(fix_date_column)

#Create a flag column to indicate rows with missing or inconsistent data. And
#Remove rows with amount zero & no values in other columns.
def create_flag_and_remove_invalid(df):
    df['Data_Flag'] = df.apply(lambda row: 1 if row.isnull().any() or row['Amount'] == 0 else 0, axis=1)
    df_cleaned = df[df['Amount'] != 0].dropna()
    return df_cleaned
    print(create_flag_and_remove_invalid)

#Clean the text in the City column.
def clean_city_column(df):
    df['City'] = df['City'].str.strip().str.title()
    return df
    print(clean_city_column)

#Bring Region Name and country from Region Master to sales data.
def clean_region_column(df):
    df['Region Name'] = df['Region Name'].str.strip().str.title()
    return df
    print(clean_region_column)

# Bring Region Name and country from Region Master to sales data.
def bring_region_info(df, region_df):
    df = df.merge(region_df[['Region_ID', 'Region Name', 'Country']], on='Region_ID', how='left')
    return df
    print(bring_region_info)

#Bring category from product Master to sales data.
def bring_category_info(df, product_df):
    df = df.merge(product_df[['Product_ID', 'Category']], on='Product_ID', how='left')
    return df
    print(bring_category_info)

#Bring category from product Master to sales data.
def calculate_country_sales(df):
    country_sales = df.groupby('Country')['Amount'].sum().reset_index()
    return country_sales
    print(calculate_country_sales)

#Calculate Country-wise Sales amount.
def group_by_car_make(df):
    car_make_sales = df.groupby('Car Make')['Amount'].sum().reset_index()
    return car_make_sales
    print(group_by_car_make)

# Validate the Date column for invalid dates and log them in a separate
#DataFrame.
def validate_dates(df):
    invalid_dates = df[df['Date'].isna()]
    logger.info(f"Invalid dates found: {invalid_dates}")
    return invalid_dates

# Handle duplicates by keeping the latest entry based on the Date column
def handle_duplicates(df):
    df_sorted = df.sort_values(by='Date', ascending=False)
    df_unique = df_sorted.drop_duplicates(subset='Product', keep='first')
    return df_unique
    print(handle_duplicates)

#. Use fuzzy matching for integrating Region Name if there are slight mismatches in
#keys.
def integrate_region_with_fuzzy_matching(df, region_df):
    df['Region Name'] = df['Region Name'].apply(
        lambda x: process.extractOne(x, region_df['Region Name'])[0] if isinstance(x, str) else x
    )
    return df

# Calculate the percentage contribution of each product to the total sales
def calculate_percentage_contribution(df):
    total_sales = df['Amount'].sum()
    df['Percentage Contribution'] = (df['Amount'] / total_sales) * 100
    return df
    print(calculate_percentage_contribution)

# Identify the top-performing product (Car Make) in each region.
def top_performing_products(df):
    top_performers = df.groupby(['Region Name', 'Car Make'])['Amount'].sum().reset_index()
    top_performers = top_performers.loc[top_performers.groupby('Region Name')['Amount'].idxmax()]
    return top_performers
    print(top_performers)

# Calculate quarterly sales trends for each Car Make.
def calculate_quarterly_sales(df):
    df['Quarter'] = df['Date'].dt.to_period('Q')
    quarterly_sales = df.groupby(['Quarter', 'Car Make'])['Amount'].sum().reset_index()
    return quarterly_sales
    print(quarterly_sales)
    print(df)

output_filename = "Sales_Data1_cleaned.xlsx"
df.to_excel(output_filename, index=False)

# Trigger the download
files.download(output_filename)
