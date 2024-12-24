# Sales_Analysis

Task: Sales Analysis for a Store
Step 1: Simulate the Dataset
Create a dataset for a store's daily sales for 1 year (365 days).
Use NumPy to generate random data:
Date: Create dates for one year starting from January 1, 2023.
Product: Randomly select from ['A', 'B', 'C', 'D'] for each day.
Units Sold: Random integers between 1 and 100.
Price Per Unit: Random floats between 5.0 and 50.0.
Step 2: Load Data into Pandas
Combine the generated data into a Pandas DataFrame with the columns: Date, Product, Units Sold, and Price Per Unit.
Step 3: Perform Analysis
Add a new column Total Sales = Units Sold × Price Per Unit.
Calculate:
Total sales for the year.
Total sales for each product.
Average daily sales.
Best-selling product (highest total sales).
Find the day with the highest total sales and the product sold on that day.
Step 4: Export the Data
Save the DataFrame to a CSV file named store_sales.csv.
