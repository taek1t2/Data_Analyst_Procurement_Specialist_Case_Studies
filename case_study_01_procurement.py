# Case Study 1 is based on procurement spending


import pandas as pd

# how to read csv in a csv file / Test Mode
facility_df = pd.read_csv("facilities.csv")
df = facility_df.shape

po_df = pd.read_csv("purchase_orders.csv")


# Which vendors made the most purchase orders?
high_value_orders = po_df["Total_Cost"] > 50000
high_value_purchase_orders = po_df[high_value_orders]


# Creating another CSV file
high_value_purchase_orders.to_csv("high_value_POs.csv", index=False)
vendor_purchase_order_counts = (
    high_value_purchase_orders
    .groupby('Vendor')
    .size()
    .sort_values(ascending=False),
)


# ==============================================
# Which vendors received the highest procurement spend ?
# ==============================================

# Group purchase orders by vendors
# Calculate total spend for each vendor
# Sort vendors from highest to lowest spend
vendor_spend = (
    po_df
    .groupby("Vendor")["Total_Cost"]
    .sum()
    .sort_values(ascending=False)
)

# Print the results
print(f"Total purchase orders: \n{vendor_spend}")

# Export the report as a CSV
vendor_spend.to_csv("vendor_spend.csv", header=["Total_Spend"])




