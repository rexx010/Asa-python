from datetime import datetime
class patient(object):
    def __init__(self, firstname, lastname, age, gender, dob, address, email, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.dob = dob
        self.address = address
        self.email = email
        self.phone = phone
        self.medicalrecord_history = []

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Firstname must be a non-empty string")
        self._firstname = value

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Lastname must be a non-empty string")
        self._lastname = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Age must be a positive integer")
        self._age = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Gender must be a non-empty string")
        self._gender = value

    @property
    def dob(self):
        return self._dob

    @dob.setter
    def dob(self, value):
        try:
            datetime.strptime(value, "%d, %m, %Y")
        except ValueError:
            raise ValueError("DOB must be in the format 'DD, MM, YYYY'")
        self._dob = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Address must be a non-empty string")
        self._address = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Email must be a non-empty string")
        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Phone must be a non-empty string")
        if not value.isdigit() or len(value) != 11:
            raise ValueError("Phone must be a string of 11 digits")
        self._phone = value

    def add_medical_record(self, record):
        if not isinstance(record, str) or not record.strip():
            raise ValueError("Medical record must be a non-empty string")
        self.medicalrecord_history.append(record)



