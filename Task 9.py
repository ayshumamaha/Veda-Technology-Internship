"""
Contact Book Using Dictionaries
Task 10 - Python Programming Track

A simple command-line contact book that supports adding, searching,
updating, and deleting contacts. Each contact is stored in a dictionary
using the phone number as its unique key.
"""

contacts = {
    "9876543210": {"name": "Alice", "email": "alice@example.com"},
    "9123456780": {"name": "Bob", "email": "bob@example.com"},
}


def add_contact():
    """Add a new contact, preventing duplicate phone numbers."""
    phone = input("Enter phone number: ").strip()

    if not phone:
        print("Phone number cannot be empty.")
        return

    if phone in contacts:
        print("A contact with this phone number already exists.")
        return

    name = input("Enter name: ").strip()
    email = input("Enter email address: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    contacts[phone] = {"name": name, "email": email}
    print("Contact added successfully.")


def search_contact():
    """Find a contact by phone number."""
    phone = input("Enter phone number to search: ").strip()
    contact = contacts.get(phone)

    if contact:
        print("\nContact found:")
        print(f"Phone: {phone}")
        print(f"Name:  {contact['name']}")
        print(f"Email: {contact['email']}")
    else:
        print("Contact not found.")


def update_contact():
    """Update an existing contact's details."""
    phone = input("Enter phone number of the contact to update: ").strip()

    if phone not in contacts:
        print("Contact not found.")
        return

    print("Press Enter to keep the current value.")
    name = input(f"Name [{contacts[phone]['name']}]: ").strip()
    email = input(f"Email [{contacts[phone]['email']}]: ").strip()

    if name:
        contacts[phone]["name"] = name
    if email:
        contacts[phone]["email"] = email

    print("Contact updated successfully.")


def delete_contact():
    """Delete a contact by phone number."""
    phone = input("Enter phone number of the contact to delete: ").strip()

    if phone not in contacts:
        print("Contact not found.")
        return

    confirmation = input(
        f"Delete {contacts[phone]['name']} ({phone})? (y/n): "
    ).strip().lower()

    if confirmation == "y":
        del contacts[phone]
        print("Contact deleted successfully.")
    else:
        print("Deletion cancelled.")


def view_contacts():
    """Display all saved contacts."""
    if not contacts:
        print("The contact book is empty.")
        return

    print("\n--- All Contacts ---")
    for phone, contact in sorted(contacts.items()):
        print(
            f"Name: {contact['name']} | "
            f"Phone: {phone} | Email: {contact['email']}"
        )


def main():
    """Run the contact-book menu until the user exits."""
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            view_contacts()
        elif choice == "6":
            print("Thank you for using the Contact Book!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nContact Book closed.")
