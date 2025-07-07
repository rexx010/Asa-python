from movie_function import *
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # This runs before each test
        global movies  # Assuming movies is a global list in movie_function.py
        movies.clear()  # Reset the movie list

    def test_that_movie_list_is_empty(self):
        self.assertNotEqual(len(add_movie("Lagbaja")), 0)

    def test_that_movie_list_is_not_empty(self):
        self.assertEqual(1, len(add_movie("Lagbaja")))
        self.assertEqual(2, len(add_movie("Coming to America")))

    def test_that_movie_can_be_rated(self):
        add_movie("Lagbaja")
        self.assertEqual(["Lagbaja", 4.0], movie_rate("Lagbaja", 4))
        self.assertEqual(["Lagbaja", 8.0], movie_rate("Lagbaja", 4))

    def test_that_rate_is_not_negative(self):
        add_movie("Lagbaja")
        self.assertEqual("invalid rate input", movie_rate("Lagbaja", 9))

    def test_that_rate_is_not_greater_than_five(self):
        add_movie("Lagbaja")
        self.assertEqual("invalid rate input", movie_rate("Lagbaja", 6))

    def test_that_movie_can_be_found(self):
        add_movie("Lagbaja")
        add_movie("Coming to America")
        self.assertEqual("Movie not found", movie_rate("Lagbaj", 4))

    def test_that_movie_rating_can_be_viewd(self):
        add_movie("Lagbaja")
        movie_rate("Lagbaja", 4)
        add_movie("Coming to America")
        movie_rate("Coming to America", 5)
        self.assertEqual(4.0, average_rating_for_a_movie("Lagbaja"))
        self.assertEqual(5.0, average_rating_for_a_movie("Coming to America"))
        add_movie("The Lord of the Rings")
        movie_rate("The Lord of the Rings", 3)
        self.assertEqual(3.0, average_rating_for_a_movie("The Lord of the Rings"))
        movie_rate("Lagbaja", 2)
        self.assertEqual(3.0, average_rating_for_a_movie("Lagbaja"))
        movie_rate("Coming to America", 4)
        self.assertEqual(4.5, average_rating_for_a_movie("Coming to America"))

    def test_that_movie_rating_is_not_zero(self):
        add_movie("Lagbaja")
        movie_rate("Lagbaja", 5)
        self.assertNotEqual(0.0, average_rating_for_a_movie("Lagbaja"))

    def test_that_movie_rating_for_all_movie_can_be_viewed(self):
        add_movie("Lagbaja")
        movie_rate("Lagbaja", 4)
        add_movie("Coming to America")
        movie_rate("Coming to America", 5)
        add_movie("The Lord of the Rings")
        movie_rate("The Lord of the Rings", 3)
        movie_rate("The Lord of the Rings", 5)
        movie_rate("Coming to America", 2)
        self.assertEqual([['Lagbaja', 4.0],['Coming to America', 7.0],['The Lord of the Rings', 8.0]], Average_rating_for_all_movies())
