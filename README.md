# NbaDataSorter

# DataSorter
Used for Practice Sorting Data with Python and SQL

### First Steps ###

https://plotly.com/python/text-and-annotations/

Get it to work for just Python, will be a good task to learn functions, loops, etc in Python. 

#Steps and Functions#

1. Find a dataset to use for data manipulation, the more columns and data the better and save this file locally
2. Set up file structure for this project (Python file and Excel file??) - May just need python file
3. Do different types of SQL and Python sorts using Pandas (Example: Top 10 prices, Last 10 days, First 10 items, etc)
4. Graph it??
5. Read the Excel file in Python (using Pandas).

Store the data in a SQL database (e.g., SQLite, which is built into Python).

Use SQL to query and sort the data.

(Optional) Export the sorted data back to Excel.


Example: import pandas as pd
import sqlite3

# Step 1: Load Excel file
df = pd.read_excel('your_file.xlsx')  # Make sure the file is in the same directory or give full path

# Step 2: Connect to SQLite (in-memory or file-based)
conn = sqlite3.connect(':memory:')  # Use ':memory:' for temporary DB or 'your_db.db' for a file
df.to_sql('data_table', conn, index=False, if_exists='replace')

# Step 3: Query and sort using SQL

#Can use multiple queries just comment out the ones you do not want to use -- This will be good SQL Practice
query = '''
SELECT * FROM data_table
ORDER BY Age ASC, Name ASC  -- Replace with your actual column names and use different queries
'''
sorted_df = pd.read_sql_query(query, conn)

# Step 4: Export to new Excel file
sorted_df.to_excel('sorted_output.xlsx', index=False)

# Cleanup
conn.close()