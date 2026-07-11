import pandas as pd

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

