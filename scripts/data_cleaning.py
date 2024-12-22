import pandas as pd

# Load the dataset
file_path = '../data/ecommerce_data.csv'
data = pd.read_csv(file_path)

# Step 1: Handle Missing Values
# Drop rows with missing CustomerID (optional, depending on analysis needs)
data = data.dropna(subset=['CustomerID'])

# Fill missing values in Description with 'Unknown'
data['Description'] = data['Description'].fillna('Unknown')

# Step 2: Remove Invalid Data
# Remove rows with negative Quantity or Unitprice
data = data[(data['Quantity'] > 0) & (data['UnitPrice'] > 0)]

# Step 3: Convert InvoiceDate to Datetime
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

# Step 4: Create New Columns
# Calculate Total Amount for each transaction
data['Total Amount'] = data['Quantity'] * data['UnitPrice']

# Preview cleaned dataset
print("Cleaned Dataset Preview")
print(data.head())
print("Cleaned Dataset Info:")
print(data.info())
print("Summary Statistics:")
print(data.describe())

# Save cleaned data to a new CSV file
data.to_csv('../data/ecommerce_data_cleaned.csv', index=False)
print("Cleaned data saved to ecommerce_data_cleaned.csv")
