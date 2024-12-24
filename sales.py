import numpy as np
import pandas as pd 
import csv

# Create a dataset for a store's daily sales for 1 year (365 days).

# Creating date for one year starting from Jan 01 2023.
start_date =  np.datetime64('2023-01-01')
end_date = np.datetime64('2023-12-31')
# Calculate the number of days
delta_days = (end_date - start_date).astype('timedelta64[D]').astype(int)
# Generate random number of days within that range
random_days = np.random.randint(1,delta_days,size=365)
# Add those random days to the start_date to get random dates
dates = start_date + random_days.astype('timedelta64[D]')

# Selecting a product 
product = np.random.choice(['A','B','C','D'],size=len(dates))

# Units sold : random integers between 1 to 100
Units_sold = np.random.choice(range(1,101,1),size=len(dates))

# Allocating price per units

Price = np.random.uniform(5,51,365)
Price_per_units = np.round(Price,2)

# Load data into pandas

Data={
    "DATE":dates,
    "Product":product,
    "Units_Sold":Units_sold,
    "Price_per_units":Price_per_units
}

dataframe = pd.DataFrame(Data)

# Performance Analysis

# Adding new columns Total sales
dataframe['Total_Sales'] = dataframe['Units_Sold']*dataframe['Price_per_units']


Sum = 0

# Total sales for the year.
Total_Sales_By_Year = dataframe['Total_Sales'].sum()
# Total sales for each product.
Total_Sales_For_Each_Product = dataframe.groupby('Product')['Total_Sales'].sum()
# Average daily sales.
Average_Sales = dataframe['Total_Sales'].mean()

# Best-selling product (highest total sales).
# Best_Selling =max(Total_Sales_For_Each_Product)
best_selling_product = Total_Sales_For_Each_Product.idxmax()

# Highest sales day in a year
highest_sales_day = dataframe.loc[dataframe['Total_Sales'].idxmax()]

dataframe.to_csv("sales_data.csv",index=False)
