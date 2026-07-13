import pandas as pd
import random
from datetime import datetime, timedelta

facilities = [
    ["DEN01", "Denver Operations Center", "Denver", "CO"],
    ["PHX01", "Phoenix Distribution Center", "Phoenix", "AZ"],
    ["SLC01", "Salt Lake Service Hub", "Salt Lake City", "UT"],
    ["RNO01", "Reno Operations Center", "Reno", "NV"],
    ["ABQ01", "Albuquerque Distribution Center", "Albuquerque", "NM"]
]

facility = pd.DataFrame(
    facilities,
    columns=["Facility ID", "Facility Name", "City", "State"]
)

facility_created = facility.to_csv("facilities.csv", index=False)


vendors = [
    ["AIS", "Atlas Industrial Suppy", "Electrical"],
    ["MHS", "Mountain HVAC Solutions", "HVAC"],
    ["SSC", "Summit Safety Co.", "Safety"],
    ["PP", "Precision Plumbing", "Plumbing"],
    ["WNS", "Western Network Systems", "Networking"],
    ["PIT", "Prime Industrial Tools", "Tools"],
    ["BOS", "BluePeak Office Supply", "Office"],
    ["IGM", "IronGate Mechanical", "Mechanical"],
    ["CWS", "CleanWorks Supply", "Janitorial"],
    ["RMF", "Rocky Mountain Fasteners", "Hardware"]
]

vendors_data = pd.DataFrame(
    vendors,
    columns=["Vendor ID", "Vendor Name", "Category"]
)

vendors_created = vendors_data.to_csv("Vendors.csv", index=False)


inventory_list = [
    ["Electrical Cable", "Electrical", 540, 200],
    ["Circuit Breaker", "Electrical", 120, 60],
    ["HVAC Filter", "HVAC", 300, 120],
    ["Safety Gloves", "Safety", 1100, 500],
    ["Safety Helmet", "Safety", 280, 120],
    ["Ethernet Switch", "Networking", 70, 20],
    ["PVC Pipe", "Plumbing", 450, 150],
    ["Power Drill", "Tools", 55, 15],
    ["Cleaning Solution", "Janitorial", 800, 250],
    ["Steel Bolts", "Hardware", 5000, 2000]
]

inventory_data = pd.DataFrame(
    inventory_list,
    columns=["Item", "Category", "Inventory Count", "Reorder Count"]
)

inventory_created = inventory_data.to_csv("inventory.csv", index=False)



purchase_orders = []

vendors = vendors_data["Vendor Name"].tolist()
facilities = facility["Facility Name"].tolist()

categories = [
    "Electrical",
    "HVAC",
    "Safety",
    "Networking",
    "Plumbing",
    "Office",
    "Mechanical",
    "Janitorial",
    "Hardware"
]

for i in range(1, 501):
    order_date = datetime(2020, 7, 12) + timedelta(days=random.randint(0, 365))
    lead_time = random.randint(5, 30)
    delivery  = order_date + timedelta(days=lead_time)
    quantity = random.randint(1, 75)
    unit_price = random.randint(25,900)
    purchase_orders.append([
        f"PO{i:05}",
        random.choice(vendors),
        random.choice(facilities),
        random.choice(categories),
        quantity,
        unit_price,
        quantity * unit_price,
        order_date.date(),
        delivery.date()
    ])

po_df = pd.DataFrame(
    purchase_orders,
    columns=[
        "PO_Number",
        "Vendor",
        "Facility",
        "Category",
        "Quantity",
        "Unit_Cost",
        "Total_Cost",
        "Order_Date",
        "Delivery_Date"
    ]
)

po_df.to_csv("purchase_orders.csv", index=False)

