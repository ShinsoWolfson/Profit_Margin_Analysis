import pandas as pd

# Load the dataset
file_path = '../data/ecommerce_data.csv'
data = pd.read_csv(file_path)

# Inspect the dataset
print("Dataset Preview:")
print(data.head())
print("Dataset Info:")
print(data.info())
print("Summary Statistics:")
print(data.describe())
print("Missing Values:")
print(data.isnull().sum())
