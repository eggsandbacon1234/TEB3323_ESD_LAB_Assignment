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
            print("Add Product Selected")

        elif choice == "2":
            print("View Products Selected")

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