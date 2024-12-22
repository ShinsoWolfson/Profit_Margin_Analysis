import pandas as pd

# Load the dataset
file_path = '../data/ecommerce_data_cleaned.csv'  # Update with your actual file path
data = pd.read_csv(file_path)

# Strip column names to remove any leading/trailing spaces
data.columns = data.columns.str.strip()

# Step 1: Add Cost and Profit Calculations (Assuming 50% Cost-to-Sales Ratio)
data['Cost'] = data['Total Amount'] * 0.5
data['Profit'] = data['Total Amount'] - data['Cost']
data['Profit Margin (%)'] = (data['Profit'] / data['Total Amount']) * 100

# Step 2: Aggregate by 'Description'
product_analysis = data.groupby('Description').agg({
    'Total Amount': 'sum',
    'Profit': 'sum',
    'Profit Margin (%)': 'mean',
    'Quantity': 'sum'
}).sort_values(by='Profit', ascending=False)

# Step 3: Save Aggregated Data
product_analysis.to_csv('../data/product_analysis.csv', index=True)
print("Product analysis saved to 'product_analysis.csv'")

# Step 4: Display Top 10 Products by Profit
print("\nTop 10 Products by Profit:")
print(product_analysis.head(10))
