contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("✅ Contact added successfully!")

def view_contacts():
    if not contacts:
        print("📭 No contacts to display.")
        return
    print("\n📋 Contact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    keyword = input("🔍 Enter name or phone to search: ")
    found = False
    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            print("\n📞 Contact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break
    if not found:
        print("❌ Contact not found.")

def update_contact():
    name = input("✏️ Enter name of contact to update: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Leave blank to keep existing value.")
            contact["phone"] = input(f"New phone [{contact['phone']}]: ") or contact["phone"]
            contact["email"] = input(f"New email [{contact['email']}]: ") or contact["email"]
            contact["address"] = input(f"New address [{contact['address']}]: ") or contact["address"]
            print("✅ Contact updated successfully!")
            return
    print("❌ Contact not found.")

def delete_contact():
    name = input("🗑️ Enter name of contact to delete: ")
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            del contacts[i]
            print("🗑️ Contact deleted successfully!")
            return
    print("❌ Contact not found.")

def main():
    print("📱 Welcome to Contact Management System")
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

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
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
