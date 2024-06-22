import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.contacts = {}

        self.create_widgets()

    def create_widgets(self):
        # Create frames
        self.frame1 = tk.Frame(self.root, bg="gray")
        self.frame1.pack(fill="x")

        self.frame2 = tk.Frame(self.root, bg="gray")
        self.frame2.pack(fill="x")

        self.frame3 = tk.Frame(self.root, bg="gray")
        self.frame3.pack(fill="x")

        # Create labels and entries
        tk.Label(self.frame1, text="Contact Name:", bg="gray").pack(side="left")
        self.name_entry = tk.Entry(self.frame1, width=30)
        self.name_entry.pack(side="left")

        tk.Label(self.frame2, text="Phone Number:", bg="gray").pack(side="left")
        self.phone_entry = tk.Entry(self.frame2, width=30)
        self.phone_entry.pack(side="left")

        tk.Label(self.frame2, text="Email:", bg="gray").pack(side="left")
        self.email_entry = tk.Entry(self.frame2, width=30)
        self.email_entry.pack(side="left")

        tk.Label(self.frame3, text="Address:", bg="gray").pack(side="left")
        self.address_entry = tk.Entry(self.frame3, width=30)
        self.address_entry.pack(side="left")

        # Create buttons
        tk.Button(self.frame1, text="Add Contact", command=self.add_contact).pack(side="left")
        tk.Button(self.frame1, text="View Contacts", command=self.view_contacts).pack(side="left")
        tk.Button(self.frame1, text="Search Contact", command=self.search_contact).pack(side="left")
        tk.Button(self.frame1, text="Update Contact", command=self.update_contact).pack(side="left")
        tk.Button(self.frame1, text="Delete Contact", command=self.delete_contact).pack(side="left")

        # Create text box for displaying contacts
        self.contacts_text = tk.Text(self.root, width=40, height=10)
        self.contacts_text.pack(fill="both", expand=True)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            self.contacts_text.insert("end", f"{name}: {phone}\n")
            self.name_entry.delete(0, "end")
            self.phone_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.address_entry.delete(0, "end")
        else:
            messagebox.showerror("Error", "Please enter contact name and phone number!")

    def view_contacts(self):
        self.contacts_text.delete(1.0, "end")
        for name, details in self.contacts.items():
            self.contacts_text.insert("end", f"{name}: {details['phone']}\n")

    def search_contact(self):
        search_term = self.name_entry.get()
        found = False

        for name, details in self.contacts.items():
            if search_term in name or search_term in details["phone"]:
                self.contacts_text.delete(1.0, "end")
                self.contacts_text.insert("end", f"Found contact: {name} - {details['phone']}\n")
                found = True

        if not found:
            self.contacts_text.delete(1.0, "end")
            self.contacts_text.insert("end", "Contact not found!")

    def update_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            self.contacts_text.delete(1.0, "end")
            self.contacts_text.insert("end", f"Contact {name} updated successfully!")
        else:
            self.contacts_text.delete(1.0, "end")
            self.contacts_text.insert("end", "Contact not found!")

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            self.contacts_text.delete(1.0, "end")
            self.contacts_text.insert("end", f"Contact {name} deleted successfully!")
        else:
            self.contacts_text.delete(1.0, "end")
            self.contacts_text.insert("end", "Contact not found!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Contact Book")
    contact_book = ContactBook(root)
    root.mainloop()