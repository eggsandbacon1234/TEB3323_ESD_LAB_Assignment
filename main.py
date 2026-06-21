import os
import csv

#Define the function to create the csv file
def create_inventory_file():
    with open("inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "product_id",
            "product_name",
            "unit_price",
            "stock_qty"
        ])

if not os.path.exists("inventory.csv"):
    create_inventory_file()
    print("inventory.csv created!")
else:
    print("inventory.csv already exists.")