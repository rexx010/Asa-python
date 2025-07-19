from stri import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_check_that_a_word_can_be_added_to_an_equally_divided_word(self):
        self.assertEqual("giceve",divide_word("give"))

    def test_check_that_word_cant_be_equally_divided(self):
        self.assertEqual("nutce",divide_word("nut"))

    def test_check_that_the_length_of_the_word_is_even(self):
        self.assertEqual(6,len(divide_word("nice")))

    def test_check_that_the_length_of_the_word_is_odd(self):
        self.assertEqual(5,len(divide_word("nic")))

    def test_check_that_the_length_of_the_word_is_not_odd(self):
        self.assertTrue(6,len(divide_word("nice")))