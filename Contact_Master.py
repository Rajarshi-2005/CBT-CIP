def add_contact(contacts):
  name = input("Enter name: ")
  phone_number = input("Enter phone number: ")
  email = input("Enter email (optional): ")
  address = input("Enter address (optional): ")

  contact = {
      "name": name,
      "phone_number": phone_number,
      "email": email,
      "address": address
  }
  contacts.append(contact)
  print("Contact added successfully!")

def delete_contact(contacts):
  name = input("Enter name of the contact to delete: ")
  found = False
  for i in range(len(contacts)):
    if contacts[i]["name"] == name:
      del contacts[i]
      found = True
      break
  if found:
    print("Contact deleted successfully!")
  else:
    print("Contact not found.")

def search_contact(contacts):
  name = input("Enter name of the contact to search: ")
  found = False
  for contact in contacts:
    if contact["name"] == name:
      print("Name:", contact["name"])
      print("Phone number:", contact["phone_number"])
      print("Email:", contact["email"])
      print("Address:", contact["address"])
      found = True
      break
  if not found:
    print("Contact not found.")

def display_contacts(contacts):
  """Displays all contacts in the contact book."""
  if not contacts:
    print("Contact book is empty.")
  else:
    print("Contacts:")
    for i, contact in enumerate(contacts, start=1):
      print(f"{i}. Name: {contact['name']}, Phone: {contact['phone_number']}")

def main():
  contacts = []

  while True:
    print("\nContact Book Menu")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Search contact")
    print("4. Display contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      add_contact(contacts)
    elif choice == "2":
      delete_contact(contacts)
    elif choice == "3":
      search_contact(contacts)
    elif choice == "4":
      display_contacts(contacts)
    elif choice == "5":
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()