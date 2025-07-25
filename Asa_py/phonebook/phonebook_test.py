from phonebook import *
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.my_phonebook = phonebook()

    def test_that_contact_can_be_created(self):
        self.my_phonebook.add_contact("Dami", "Doe", "12345678901", "123 Main St")
        self.assertEqual(len(self.my_phonebook.contacts), 1)


