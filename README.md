## Sales Data Cleaning & Analysis (Python)

This project demonstrates an end-to-end sales data cleaning and preprocessing pipeline using Python.
It automates the tedious manual work of cleaning Excel files and transforms raw, inconsistent sales records into structured, ready-to-analyze datasets.

## Problem Statement

Sales teams often receive data that is:
- Full of missing values
- Incorrectly formatted (dates, city names, product info)
- Spread across multiple files without integration
Such issues delay reporting and lead to wrong decisions.
This project solves the problem by creating a reusable Python pipeline to standardize, validate, and enrich sales data.

## Tools & Technologies

Python → pandas, numpy, fuzzywuzzy, openpyxl
Excel (XLSX) → Input and cleaned output files
Logging → For error tracking and validation

## Key Features

✔ - Removes null rows & invalid records
✔ - Splits product details into Car Make & Car Model
✔ - Fixes inconsistent date formats
✔ - Cleans text fields (City, Region)
✔ - Integrates Region & Country from master data
✔ - Adds Product Category mapping
✔ - Handles duplicates (keeps latest entry)
✔ - Fuzzy matches regions to reduce human errors
✔ - Calculates:

- Country-wise sales
- % contribution of each product
- Top-performing car make per region
- Quarterly sales trends

##  Repository Structure
- `/data` → Raw Sales Excel files  
- [`/output`](https://github.com/Junaid30121997/Sales-Data-Cleaning-Python/blob/main/Sales_Data_.xlsx) → Cleaned & processed Excel files  
- [`sales_cleaning.py` ](https://github.com/Junaid30121997/Sales-Data-Cleaning-Python/blob/main/Python%20Code.py)→ Python script containing reusable functions  
- pandas
numpy
fuzzywuzzy
openpyxl→ Required Python libraries  
- [`/docs`](https://github.com/Junaid30121997/Sales-Data-Cleaning-Python/blob/main/Python%20Test%20.pdf) → Reference PDF (tasks & instructions)

## Impact & Results

- Reduced manual data cleaning time by 70%
- Improved accuracy of sales reporting by automating validation
- Delivered ready-to-use Excel outputs for business teams

## About the Project

This project highlights my ability to:
- Work with messy real-world data
- Build ETL-like data cleaning pipelines in Python
- Apply fuzzy matching, data validation, and master-data integration
- Provide clean datasets for reporting, dashboards, and decision-making

## Connect with Me

 - LinkedIn: https://www.linkedin.com/in/mohammadjunaidahmed/
 - GitHub Portfolio: https://github.com/Junaid30121997
 - Email: mohammedjunaid689@gmail.com







