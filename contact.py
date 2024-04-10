contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print("Contact added successfully.")

def view_contacts():
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")

def search_contact():
    search_type = input("Search by name or phone number? (name/phone): ")
    search_value = input("Enter search value: ")
    if search_type.lower() == 'name':
        if search_value in contacts:
            print(f"Name: {search_value}, Phone: {contacts[search_value]['phone']}")
        else:
            print("Contact not found.")
    elif search_type.lower() == 'phone':
        for name, details in contacts.items():
            if details['phone'] == search_value:
                print(f"Name: {name}, Phone: {details['phone']}")
                break
        else:
            print("Contact not found.")
    else:
        print("Invalid search type.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Enter new details:")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
