# Case Study 1 is based on procurement spending


import pandas as pd

# how to read csv in a csv file / Test Mode
facility_df = pd.read_csv("facilities.csv")
df = facility_df.shape
# print(df)


po_df = pd.read_csv("purchase_orders.csv")

# Finding the highest total cost
print(po_df.Total_Cost.max())

# Which vendors made the most purchase orders?
high_value_orders = po_df["Total_Cost"] > 50000
high_value_purchase_orders = po_df[high_value_orders]
result_vendor = po_df[high_value_orders].groupby('Vendor')

# vendor_counts = result_vendor.size()
# print(vendor_counts.sort_values())

# Creating another CSV file
high_value_purchase_orders.to_csv("high_value_POs.csv", index=False)
vendor_purchase_order_counts = (
    result_vendor,
    high_value_purchase_orders
    .groupby('Vendor')
    .size()
    .sort_values(ascending=False),
)

print(vendor_purchase_order_counts)
