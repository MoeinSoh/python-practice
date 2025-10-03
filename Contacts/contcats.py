import json

class Contacts:
    def __init__(self, name="", number="", email=""):
        self.name = name
        self.number = number
        self.email = email

    def get_info(self):
        self.name = input("Name: ")
        self.number = input("Phone Number: ")
        self.email = input("Email: ")

    def add_contacts(self, file):
        with open(file, 'r') as f:
            contacts = json.load(f)

            new_contact = {
                "name": self.name,
                "number": self.number,
                "email": self.email
            }

            contacts.append(new_contact)
        with open(file, 'w') as f:
            json.dump(contacts, f, indent=4)

c = Contacts()
c.get_info()
c.add_contacts("naruto_contacts.json")





