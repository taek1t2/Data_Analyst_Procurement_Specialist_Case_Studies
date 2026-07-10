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

print(facility_created)
