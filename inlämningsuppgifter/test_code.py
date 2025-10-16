# """
# args:
# Create a 
# cless named ContactBaook
# - create methode on it :
# methodes:
# - add_contact
# - View all contacts.
# - Search for a contact by name.
# - Remove a contact.
# """

# class ContactBook:
#     def __init__(self):
#         self.contact = {}
    
#     def add_contact(self, name, phone, email):
#         if name in self.contact:
#             print(f"Contact: {name} found in contactbook")
#             overwrite = input("Overwrite it? (ye/no)").lower()
#             if overwrite != "yes":
#                 print("Contact not found")
#             return
#         """Add contact här"""
#         self.add_contact[name] = {
#             "phone": phone,
#             "email": email
#         }
#         print(f"Contact: {name} added succefully")

#         """Shows all contacts in the contactbook"""

#     def view_all_contacts(self):
#         if not self.contact:
#             print("Contactbook is empty")
#             return
        
#         print("In" + "=" * 60)
#         print("All contacts")
#         print("=" * 60)

#         for name, info in sorted(self.contact.items()):
#             print(f"Name: {name}")
#             print(f"Phone: {info['phone']}")
#             print(f"Email: {info['email']}")
#             print("-" * 60)

#     def searsh_contact(self, name):
#         if name in self.contact:
#             print("\n" + "="*60)
#             print("CONTACT FOUND")
#             print("-"*60)
#             print(f"Name: {name}")
#             print(f"Phone: {self.contact[name]['phone']}")
#             print(f"Email: {self.contact[name]['email']}")
#         else:
#             print(f"contact not found")
    
#     def remouve_contact(self, name):
#         if name in self.contact:
#             del self.contact[name]
#         else:
#             print(f"Contact not found")
    
#     def display_menu():
#         print("\n" + "="*60)
#         print("CONTACT BOOK MENU")
#         print("-"*60)

#         print("1. Add a new contact")
#         print("2. View all contacts ")
#         print("3. Search for a contact")
#         print("4. Remove a contact")
#         print("5. Exit")
#         print("="*60)

#     def main():
#         contact_book = ContactBook()

#         print("\n" + "="*60)
#         print("Welcome to Contact Book Manager!")
#         print("="*60)

#         while True:
#             display_menu()
#             choice = input("Enter you choice (1-5)").strip()

#             if choice == '1':
#                 print("ADD NEW CONTACT")
#                 name = input("Enter name").strip()
#                 if not name:
#                     print("Name can't be empty")
#                     continue
#                 phone = input("Enter phone number ").strip()
#                 email = input("Enter email").strip()
#                 contact_book.add_contact(name, phone, email)
            
#             elif choice == "2":
#                 contact_book.view_all_contacts()
            
#             elif choice == "3":
#                 name = input("Enter contact name to searsh").strip()
#                 if name:
#                     contact_book.searsh_contact()
#                 else:
#                     print("Contact not found")
                 
#             elif choice == "4":
#                 name = input("Enter the name to remove").strip()
#                 if name:
#                     contact_book.remouve_contact()
#                 else:
#                     print("Name not found")            
            
#             elif choice == "5":
#                 print("\n"+"="*60)
#                 print("Thank you for using contact book")
#                 print("Bye bye")
#                 print("="*60)
#                 break
#             else:
#                 print("\n❌ Invalid choice! Please enter a number between 1 and 5.")

# if __name__ == __main__
#     min()