from contact import *
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.my_contact = contact("John", "Doe", "12345678901", "123 Main St")

    def test_that_firstname_can_be_set(self):
        self.my_contact.firstname = "Femi"
        self.assertEqual(self.my_contact.firstname, "Femi")

    def test_that_firstname_raises_error_with_wrong_type(self):
        with self.assertRaises(ValueError):
            self.my_contact.firstname = 12345

    def test_that_firstname_raises_error_with_empty_string(self):
        with self.assertRaises(ValueError):
            self.my_contact.firstname = ""

    def test_that_lastname_can_be_set(self):
        self.my_contact.lastname = "Dorcas"
        self.assertEqual(self.my_contact.lastname, "Dorcas")

    def test_that_lastname_raises_error_with_wrong_type(self):
        with self.assertRaises(ValueError):
            self.my_contact.lastname = 12345

    def test_that_lastname_raises_error_with_empty_string(self):
        with self.assertRaises(ValueError):
            self.my_contact.lastname = ""

    def test_that_number_can_be_set(self):
        self.my_contact.contact_info = "12345678902"
        self.assertEqual(self.my_contact.contact_info, "12345678902")

    def test_that_number_raises_error_with_wrong_type(self):
        with self.assertRaises(ValueError):
            self.my_contact.contact_info = 1234567890

    def test_that_number_raises_error_with_empty_string(self):
        with self.assertRaises(ValueError):
            self.my_contact.contact_info = ""

    def test_that_contact_isnt_more_than_11_digits(self):
        with self.assertRaises(ValueError):
            self.my_contact.contact_info = "123456789012"

    def test_that_contact_isnt_less_than_11_digits(self):
        with self.assertRaises(ValueError):
            self.my_contact.contact_info = "123"

    def test_that_contact_only_contains_digits(self):
        with self.assertRaises(ValueError):
            self.my_contact.contact_info = "123456dg909"



if __name__ == '__main__':
    unittest.main()
