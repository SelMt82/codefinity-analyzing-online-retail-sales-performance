This file is a merged representation of the entire codebase, combined into a single document

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block or first three lines for files with .csv extensions

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- This file includes only .ipynb and .csv file contents in full or partial form
- All other file types are represented only through the directory structure
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files

# Directory Structure

````
./
fs_report.md
main.py
online_retail.csv
````

# Files

## File: online_retail.csv
````
,InvoiceNo,StockCode,Description,Quantity,InvoiceDate,UnitPrice,CustomerID,Country
0,536370,22728,ALARM CLOCK BAKELIKE PINK,24,01.12.2010 08:45,3.75,12583.0,France
1,536370,22727,ALARM CLOCK BAKELIKE RED ,24,01.12.2010 08:45,3.75,12583.0,France
````

## File: main.py
````
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load subset for performance
df = pd.read_csv("online_retail.csv")

# Your code starts here

# 1. Create a revenue column
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# 2. Group by Country and sum the revenue
revenue_by_country = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False)

# 3. Display the total revenue per country
print(revenue_by_country)
# 3. Print exact data values for the plot
print("Revenue by Country Data:", revenue_by_country.to_dict())

# 4. Plot a bar chart of total revenue by country
plt.figure(figsize=(12, 6))
sns.barplot(x=revenue_by_country.index, y=revenue_by_country.values, palette="viridis")
plt.xticks(rotation=90)
plt.ylabel("Total Revenue (GBP)")
plt.title("Total Revenue by Country")
plt.tight_layout()
plt.show()````
