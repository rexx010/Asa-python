from patient import *
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.new_patient = patient("John", "Doe", 30, "M", "01, 01, 1993", "123 Main St", "Grexx200@gmail.com", "09161171012")
    def test_that_the_patient_information_can_be_created_and_added(self):
        self.new_patient = patient("Dami", "Adeiga", 16, "M", "22, 09, 2000", "456 Elm St", "Grexx200@gmail.com", "09161171012")
        self.assertEqual(self.new_patient.firstname, "Dami")
        self.assertEqual(self.new_patient.lastname, "Adeiga")
        self.assertEqual(self.new_patient.age, 16)
        self.assertEqual(self.new_patient.gender, "M")
        self.assertEqual(self.new_patient.dob, "22, 09, 2000")
        self.assertEqual(self.new_patient.address, "456 Elm St")
        self.assertEqual(self.new_patient.email, "Grexx200@gmail.com")
        self.assertEqual(self.new_patient.phone, "09161171012")

    def test_that_the_patient_firstname_raises_error_with_wrong_firstname_type(self):
        with self.assertRaises(ValueError):
            self.new_patient.firstname = 12345

    def test_that_the_patient_firstname_raises_error_with_empty_firstname(self):
        with self.assertRaises(ValueError):
            self.new_patient.firstname = ""

    def test_that_the_patient_firstname_can_be_set(self):
        self.new_patient.firstname = "Jane"
        self.assertEqual(self.new_patient.firstname, "Jane")

    def test_that_the_patient_lastname_raises_error_with_wrong_lastname_type(self):
        with self.assertRaises(ValueError):
            self.new_patient.lastname = 12345

    def test_that_the_patient_lastname_raises_error_with_empty_lastname(self):
        with self.assertRaises(ValueError):
            self.new_patient.lastname = ""

    def test_that_the_patient_lastname_can_be_set(self):
        self.new_patient.lastname = "Smith"
        self.assertEqual(self.new_patient.lastname, "Smith")

    def test_that_the_patient_age_raises_error_with_wrong_age_type(self):
        with self.assertRaises(ValueError):
            self.new_patient.age = "twenty"

    def test_that_the_patient_age_raises_error_with_negative_age(self):
        with self.assertRaises(ValueError):
            self.new_patient.age = -5

    def test_that_the_patient_age_can_be_set(self):
        self.new_patient.age = 25
        self.assertEqual(self.new_patient.age, 25)

    def test_that_the_patient_gender_raises_error_with_wrong_gender_type(self):
        with self.assertRaises(ValueError):
            self.new_patient.gender = 1

    def test_that_the_patient_gender_raises_error_with_empty_parameter(self):
        with self.assertRaises(ValueError):
            self.new_patient.gender = ""

    def test_that_the_patient_gender_can_be_set(self):
        self.new_patient.gender = "F"
        self.assertEqual(self.new_patient.gender, "F")

    def test_that_the_patient_dob_raises_error_with_wrong_dob_type(self):
        with self.assertRaises(ValueError):
            self.new_patient.dob = '12345'

    def test_that_the_patient_dob_raises_error_with_empty_dob(self):
        with self.assertRaises(ValueError):
            self.new_patient.dob = ""

    def test_that_the_patient_dob_can_be_set(self):
        self.new_patient.dob = "01, 01, 1990"
        self.assertEqual(self.new_patient.dob, "01, 01, 1990")

    def test_that_the_patient_address_raises_error_with_wrong_address_type(self):
        with self.assertRaises(ValueError):
            self.new_patient.address = 12345

    def test_that_the_patient_address_raises_error_with_empty_address(self):
        with self.assertRaises(ValueError):
            self.new_patient.address = ""

    def test_that_the_patient_address_can_be_set(self):
        self.new_patient.address = "789 Oak St"
        self.assertEqual(self.new_patient.address, "789 Oak St")

    def test_that_the_patient_email_raises_error_with_wrong_email_type(self):
        with self.assertRaises(ValueError):
            self.new_patient.email = 12345

    def test_that_the_patient_email_raises_error_with_empty_email(self):
        with self.assertRaises(ValueError):
            self.new_patient.email = ""

    def test_that_the_patient_email_can_be_set(self):
        self.new_patient.email = "dami@gmail.com"
        self.assertEqual(self.new_patient.email, "dami@gmail.com")

    def test_that_the_patient_phone_raises_error_with_wrong_phone_type(self):
        with self.assertRaises(ValueError):
            self.new_patient.phone = 12345

    def test_that_the_patient_phone_raises_error_with_empty_phone(self):
        with self.assertRaises(ValueError):
            self.new_patient.phone = ""

    def test_that_the_patient_phone_can_be_set(self):
        self.new_patient.phone = "09161171012"
        self.assertEqual(self.new_patient.phone, "09161171012")