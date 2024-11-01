# List to store contacts
contacts = []

def show_menu():
    print("\n----- Contact Management -----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact = {"Name": name, "Phone": phone, "Email": email}
    contacts.append(contact)
    print("New contact added!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for idx, contact in enumerate(contacts):
            print(f"{idx + 1}. {contact}")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact["Name"] == name:
            print("Enter new information:")
            contact["Phone"] = input("Phone number: ")
            contact["Email"] = input("Email: ")
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact["Name"] == name:
            contacts.remove(contact)
            print("Contact deleted.")
            return
    print("Contact not found.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
