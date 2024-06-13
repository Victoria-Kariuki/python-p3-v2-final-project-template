# lib/cli.py
import models

print("Running")

def main_menu():
    print("Welcome to the Cake Management System!")
    print("1. Manage Cakes")
    print("2. Manage Clients")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        cake_menu()
    elif choice == "2":
        client_menu()
    elif choice == "3":
        exit("Exiting...")
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def cake_menu():
    print("\nCake Menu:")
    print("1. Add a Cake")
    print("2. Update a Cake")
    print("3. Delete a Cake")
    print("4. Back to Main Menu")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_cake()
    elif choice == "2":
        update_cake()
    elif choice == "3":
        delete_cake()
    elif choice == "4":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        cake_menu()

def add_cake():
    print("Add Cake Form")
    cake_type = input("Enter cake type >")
    flavour = input("Enter cake flavour >")
    client_id = input("Enter client id >")
    
    models.Cake.create(cake_type, flavour, client_id)

def update_cake():
    print("Update cake type")
    cake_type = input("Enter cake type >")
    flavour = input("Enter cake flavour >")
    client_id = input("Enter client_id >")
    
    models.Cake.update(cake_type, flavour, client_id)

    pass

def delete_cake():
    print("Delete Cake")
    cake_id = int(input("Enter cake ID to delete: "))
    
    cake = models.Cake.fetch_by_id(cake_id)
    if cake != None:
        cake.delete()



def client_menu():
    print("\nClient Menu:")
    print("1. Add a Client")
    print("2. Update a Client")
    print("3. Delete a Client")
    print("4. Back to Main Menu")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_client()
    elif choice == "2":
        update_client()
    elif choice == "3":
        delete_client()
    elif choice == "4":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        client_menu()

def add_client():
    # Logic to add a client
    pass

def update_client():
    # Logic to update a client
    pass

def delete_client():
    # Logic to delete a client
    pass

if __name__ == "__main__":
    main_menu()
