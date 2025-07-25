class contact(object):
    def __init__(self, firstname, lastname, contact, address):
        self.firstname = firstname
        self.lastname = lastname
        self.contact_info = contact
        self.address = address

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("First name must be a non-empty string")
        self._firstname = name

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Last name must be a non-empty string")
        self._lastname = name

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, number):
        if not isinstance(number, str) or not number.strip() :
            raise ValueError("Contact info must be a non-empty string")
        if not number.isdigit():
            raise ValueError("digit only is required")
        if not len(number) == 11:
            raise ValueError("length of contact info must be 11")
        self._contact_info = number

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if not isinstance(address, str) or not address.strip():
            raise ValueError("Address must be a non-empty String")