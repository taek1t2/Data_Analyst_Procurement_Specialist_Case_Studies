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
result_vendor = po_df[high_value_orders].groupby('Vendor')
