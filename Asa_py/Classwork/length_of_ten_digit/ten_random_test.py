from ten_random_number_function import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_the_length_of_the_array(self):
        self.assertEqual(the_length_of_the_list([3 ,5 ,6 ,2 ,1 ,7 ,5 ,3 ,1 ,2]),10 )

    def test_the_sum_of_odd_digit(self):
        self.assertEqual(sum_of_odd_elements([3 ,5 ,6 ,2 ,1 ,7 ,5 ,3 ,1 ,2]), 19)

    def test_the_sum_of_even_digit(self):
        self.assertEqual(the_sum_of_even_elements([3 ,5 ,6 ,2 ,1 ,7 ,5 ,3 ,1 ,2]), 16)

    def test_the_multiple_of_third_digits(self):
        self.assertEqual(elements_at_third_index([3 ,5 ,6 ,2 ,1 ,7 ,5 ,3 ,1 ,2]), 42)

    def calculate_the_average_value(self):
        self.assertEqual(calculate_all_element_average([3 ,5 ,6 ,2 ,1 ,7 ,5 ,3 ,1 ,2]), 5.5)

