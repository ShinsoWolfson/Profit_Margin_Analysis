import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the processed data
data = pd.read_csv('../data/product_analysis.csv')

# Extract top 10 products by Total Amount
top_10_products = data.nlargest(10, 'Total Amount')

# Visualization 1: Bar Chart for Top 10 Products by Total Amount
fig1 = px.bar(
    top_10_products,
    x='Description',  # Column name for x-axis
    y='Total Amount',  # Column name for y-axis
    title='Top 10 Products by Profit',
    labels={'Description': 'Product Description', 'Total Amount': 'Total Profit'},
    color='Total Amount',  # Optional: Adds gradient color based on Total Amount
)
fig1.update_layout(
    xaxis_title="Product Description",
    yaxis_title="Total Profit",
    xaxis_tickangle=45
)
fig1.show()

# Visualization 2: Pie Chart for Quantity Distribution of Top 10 Products
fig2 = px.pie(
    top_10_products,
    names='Description',
    values='Quantity',
    title='Quantity Distribution of Top 10 Products'
)
fig2.update_traces(textinfo='percent+label')  # Shows percentages with labels
fig2.show()

# Visualization 3: Line Chart of Total Amount vs. Quantity for Top 10 Products
fig3 = go.Figure()
fig3.add_trace(go.Scatter(
    x=top_10_products['Description'],
    y=top_10_products['Total Amount'],
    mode='lines+markers',
    name='Total Amount'
))
fig3.add_trace(go.Scatter(
    x=top_10_products['Description'],
    y=top_10_products['Quantity'],
    mode='lines+markers',
    name='Quantity'
))
fig3.update_layout(
    title='Total Amount vs. Quantity for Top 10 Products',
    xaxis_title='Product Description',
    yaxis_title='Values',
    xaxis_tickangle=45,
    legend_title="Metrics"
)
fig3.show()
