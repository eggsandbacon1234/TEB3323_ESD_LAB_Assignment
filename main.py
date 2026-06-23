import os
import csv

#Function to clearn the terminal
def clear_screen():
    os.system("cls")

#function to create the csv file
def create_inventory_file():
    with open("inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "product_id",
            "product_name",
            "unit_price",
            "stock_qty"
        ])

#Startup Function
def startup():

    if not os.path.exists("inventory.csv"): #If inventory.csv not exist
        create_inventory_file() #Create the csv file
        print("inventory.csv created!")

    else: #If inventory file exist
        print("\nInventory file found.") 
        print("1. Load Existing Inventory")
        print("2. Create New Inventory")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Loading inventory...")

        elif choice == "2":
            create_inventory_file()
            print("New inventory created.")

        else:
            print("Invalid choice.")

#Function to add product to the csv
def add_product():

    print("\n=== Add Product ===")

    while True:
        product_id = input("Enter Product ID: ")

        if product_id == "":
            print("Product ID cannot be empty.")
            continue

        duplicate_found = False

        with open("inventory.csv", "r") as file:
            reader = csv.reader(file)

            next(reader)  # Skip header row

            for row in reader:
                if row[0] == product_id:
                    duplicate_found = True
                    break

        if duplicate_found:
            print("Product ID already exists.")
        else:
            break

    while True:
        product_name = input("Enter Product Name: ")

        if product_name == "":
            print("Product name cannot be empty.")
        else:
            break

    while True:

        try:
            unit_price = float(input("Enter Unit Price: "))

            if unit_price < 0:
                print("Price cannot be negative.")
                continue

            break

        except ValueError:
            print("Invalid price. Please enter a valid number.")

    while True:

        try:
            stock_qty = int(input("Enter Stock Quantity: "))

            if stock_qty < 0:
                print("Stock quantity cannot be negative.")
                continue

            break

        except ValueError:
            print("Invalid stock quantity. Please enter a whole number.")

    with open("inventory.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            product_id,
            product_name,
            unit_price,
            stock_qty
    ])

    print("\nProduct Added Successfully!")

    input("\nPress Enter to return to menu...")

def view_products(): #function to view the products stored in the csv

    print("\n=== All Products ===\n")

    with open("inventory.csv", "r") as file:
        reader = csv.reader(file)

        next(reader)  # Skip header row

        print(f"{'ID':<10}{'NAME':<20}{'PRICE':<15}{'STOCK':<10}") #Print it in a better style
        print("-" * 55)

        for row in reader:
            print(f"{row[0]:<10}{row[1]:<20}{row[2]:<15}{row[3]:<10}")

    input("\nPress Enter to return to menu...")

#The CLI display menu function.
def display_menu():
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Adjust Stock")
    print("5. Low Stock Alert")
    print("6. Exit")

#Main Function
def main():
    startup() #Run the startup function first
    while True:
        clear_screen() #Call clear screen function to clear terminal so that its not messy
        display_menu() #call function to display the menu.

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product() #call add product function if option 1 is selected

        elif choice == "2":
            view_products() #call the view product function if option 2 is selected 

        elif choice == "3":
            print("Search Product Selected")

        elif choice == "4":
            print("Adjust Stock Selected")

        elif choice == "5":
            print("Low Stock Alert Selected")

        elif choice == "6":
            print("Exiting System...")
            break

        else:
            print("Invalid menu choice!")
            input("\nPress Enter to continue...")
main() #Run the main function