from contact import *
class phonebook(object):
    def __init__(self):
        self.contacts = []

    # def contacts(self):
    #     return self._contacts

    def add_contact(self, firstname, lastname, contact_info, address):
        if not isinstance(firstname, str) or not firstname.strip():
            raise ValueError("First name must be a non-empty string")
        if not isinstance(lastname, str) or not lastname.strip():
            raise ValueError("Last name must be a non-empty string")
        if not isinstance(contact_info, str) or not contact_info.strip():
            raise ValueError("Contact info must be a non-empty string")
        if not contact_info.isdigit():
            raise ValueError("Contact info must contain digits only")
        if len(contact_info) != 11:
            raise ValueError("Contact info must be exactly 11 digits long")
        if not isinstance(address, str) or not address.strip():
            raise ValueError("Address must be a non-empty string")
        self.contacts.append(contact(firstname, lastname, contact_info, address))
        return self.contacts

    def get_contacts(self):
        return self.contacts

    def remove_contact(self, phonenumber):
        if not isinstance(phonenumber, str) or not phonenumber.strip():
            raise ValueError("Phone number must be a non-empty string")
        for contact in self.contacts:
            if contact.contact_info == phonenumber:
                self.contacts.remove(contact)
                return
        raise ValueError(f"no contact with phone number {phonenumber} found")

    def find_contact_by_number(self, phonenumber):
        if not isinstance(phonenumber, str) or not phonenumber.strip():
            raise ValueError("Phone number must be a non-empty string")
        for contact in self.contacts:
            if contact.contact_info == phonenumber:
                return f"{contact.firstname} {contact.lastname} {contact.contact_info} {contact.address}"
        raise ValueError(f"no contact with phone number {phonenumber} found")

    def find_contact_by_firstname(self, firstname):
        if not isinstance(firstname, str) or not firstname.strip():
            raise ValueError("First name must be a non-empty string")
        for contact in self.contacts:
            if contact.firstname == firstname:
                return f"{contact.firstname} {contact.lastname} {contact.contact_info} {contact.address}"
        raise ValueError(f"no contact with firstname {firstname} found")

    def find_contact_by_lastname(self, lastname):
        if not isinstance(lastname, str) or not lastname.strip():
            raise ValueError("Last name must be a non-empty string")
        for contact in self.contacts:
            if contact.lastname == lastname:
                return f"{contact.firstname} {contact.lastname} {contact.contact_info} {contact.address}"
        raise ValueError(f"no contact with lastname {lastname} found")

    def find_contact_by_contact_address(self, address):
        if not isinstance(address, str) or not address.strip():
            raise ValueError("Address must be a non-empty string")
        for contact in self.contacts:
            if contact.address == address:
                return f"{contact.firstname} {contact.lastname} {contact.contact_info} {contact.address}"
        raise ValueError(f"no contact with address {address} found")

    def edit_contact(self, phonenumber, firstname, lastname, contact_info, address):
        if not isinstance(phonenumber, str) or not phonenumber.strip():
            raise ValueError("Phone number must be a non-empty string")
        for contact in self.contacts:
            if contact.contact_info == phonenumber:
                contact.firstname = firstname
                contact.lastname = lastname
                contact.contact_info = contact_info
                contact.address = address
                return "edited successfully"
        raise ValueError(f"no contact with phone number {phonenumber} found")