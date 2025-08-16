## Sales Data Cleaning & Analysis (Python)

This repository contains a **Python script** to clean and analyze sales data from Excel files.  
It automates multiple data preprocessing steps including null removal, text cleaning, merging master data, and generating analytics.


##  Features
1. Remove null rows and invalid records.  
2. Split product column into **Car Make** & **Car Model**.  
3. Fix date column (DD/MM/YYYY → Date format).  
4. Create a data flag column for missing/inconsistent rows.  
5. Clean City column text formatting.  
6. Integrate **Region Name & Country** from Region Master.  
7. Integrate **Category** from Product Master.  
8. Calculate **Country-wise Sales**.  
9. Group by **Car Make** for sales.  
10. Validate dates and log invalid entries.  
11. Handle duplicates by latest Date entry.  
12. Use fuzzy matching for Region integration.  
13. Calculate % contribution of each product.  
14. Identify **Top-performing Car Make** per region.  
15. Calculate **Quarterly Sales Trends**.  

---

##  Repository Structure
- `/data` → Raw Sales Excel files  
- `/output` → Cleaned & processed Excel files  
- [`sales_cleaning.py` ](https://github.com/Junaid30121997/Sales-Data-Cleaning-Python/blob/main/Python%20Code.py)→ Python script containing reusable functions  
- pandas
numpy
fuzzywuzzy
openpyxl→ Required Python libraries  
- [`/docs`](https://github.com/Junaid30121997/Sales-Data-Cleaning-Python/blob/main/Python%20Test%20.pdf) → Reference PDF (tasks & instructions)  

##  Tech Stack
- Python (pandas, numpy, fuzzywuzzy)  
- Excel (XLSX input/output)  
- Logging for error handling  


