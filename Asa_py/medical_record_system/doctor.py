class doctor(object):
    def __init__(self, name, contact, address, nationality, status, specialty):
        self.name = name
        self.contact = contact
        self.address = address
        self.nationality = nationality
        self.status = status
        self.specialty = specialty

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact):
        if not isinstance(contact, str) or not contact.strip():
            raise ValueError("Contact must be a non-empty string")
        self._contact = contact

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if not isinstance(address, str) or not address.strip():
            raise ValueError("Address must be a non-empty string")
        self._address = address

    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        if not isinstance(nationality, str) or not nationality.strip():
            raise ValueError("Nationality must be a non-empty string")
        self._nationality = nationality

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if not isinstance(status, str) or not status.strip():
            raise ValueError("Status must be a non-empty string")
        self._status = status

    @property
    def specialty(self):
        return self._specialty

    @specialty.setter
    def specialty(self, specialty):
        if not isinstance(specialty, str) or not specialty.strip():
            raise ValueError("Specialty must be a non-empty string")
        self._specialty = specialty