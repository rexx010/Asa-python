from doctor import *
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.my_doctor = doctor("Dr. John Doe", "1234567890", "456 Elm St", "American", "Single", "Pediatrics")

    def test_that_doctor_profile_can_be_created(self):
        doc = doctor("Dr. Smith", "1234567890", "123 Main St", "Nigerian", "Married", "Cardiology")
        self.assertEqual(doc.name, "Dr. Smith")
        self.assertEqual(doc.contact, "1234567890")
        self.assertEqual(doc.address, "123 Main St")
        self.assertEqual(doc.nationality, "Nigerian")
        self.assertEqual(doc.status, "Married")
        self.assertEqual(doc.specialty, "Cardiologist")

    def test_that_doctor_name_raises_error_with_wrong_name_type(self):
        with self.assertRaises(ValueError):
            self.my_doctor.name = 123

    def test_that_the_doctor_name_raises_error_with_empty_name(self):
        with self.assertRaises(ValueError):
            self.my_doctor.name = ""
    def test_that_the_doctor_name_can_be_set(self):
        self.my_doctor.name = "Dr. Jane Doe"
        self.assertEqual(self.my_doctor.name, "Dr. Jane Doe")

    def test_that_the_doctor_contact_raises_error_with_wrong_contact_type(self):
        with self.assertRaises(ValueError):
            self.my_doctor.contact = 1234567890

    def test_that_the_doctor_contact_raises_error_with_empty_contact(self):
        with self.assertRaises(ValueError):
            self.my_doctor.contact = ""

    def test_that_the_doctor_contact_can_be_set(self):
        self.my_doctor.contact = "0987654321"
        self.assertEqual(self.my_doctor.contact, "0987654321")

    def test_that_the_doctor_address_raises_error_with_wrong_address_type(self):
        with self.assertRaises(ValueError):
            self.my_doctor.address = 12345

    def test_that_the_doctor_address_raises_error_with_empty_address(self):
        with self.assertRaises(ValueError):
            self.my_doctor.address = ""

    def test_that_the_doctor_address_can_be_set(self):
        self.my_doctor.address = "789 Oak St"
        self.assertEqual(self.my_doctor.address, "789 Oak St")

    def test_that_the_doctor_nationality_raises_error_with_wrong_nationality_type(self):
        with self.assertRaises(ValueError):
            self.my_doctor.nationality = 12345

    def test_that_the_doctor_nationality_raises_error_with_empty_nationality(self):
        with self.assertRaises(ValueError):
            self.my_doctor.nationality = ""

    def test_that_the_doctor_nationality_can_be_set(self):
        self.my_doctor.nationality = "British"
        self.assertEqual(self.my_doctor.nationality, "British")

    def test_that_the_doctor_status_raises_error_with_wrong_status_type(self):
        with self.assertRaises(ValueError):
            self.my_doctor.status = 12345

    def test_that_the_doctor_status_raises_error_with_empty_status(self):
        with self.assertRaises(ValueError):
            self.my_doctor.status = ""

    def test_that_the_doctor_status_can_be_set(self):
        self.my_doctor.status = "Divorced"
        self.assertEqual(self.my_doctor.status, "Divorced")

    def test_that_the_doctor_specialty_raises_error_with_wrong_specialty_type(self):
        with self.assertRaises(ValueError):
            self.my_doctor.specialty = 12345

    def test_that_the_doctor_specialty_raises_error_with_empty_specialty(self):
        with self.assertRaises(ValueError):
            self.my_doctor.specialty = ""

    def test_that_the_doctor_specialty_can_be_set(self):
        self.my_doctor.specialty = "Neurology"
        self.assertEqual(self.my_doctor.specialty, "Neurology")
        


