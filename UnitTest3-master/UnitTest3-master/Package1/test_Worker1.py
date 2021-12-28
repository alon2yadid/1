from unittest import TestCase
from Worker import Worker



class TestWorker(TestCase):

    def setUp(self):
        self.alon1 = Worker("alon", "yadid", 1999, 7, 3, "modiin", "israel")

    def test_full_name(self):
        self.assertTrue(self.alon1.full_name() == f"alon yadid")

    def test_age(self):
        self.assertTrue(self.alon1.age() == "alon is 22 years old")
        self.assertTrue(self.alon1.birth_year < 2021)
        self.assertFalse(self.alon1.birth_year > 2021)
        self.assertTrue(self.alon1.birth_year != 2021)

    def test_days_to_birthday(self):
        self.assertTrue(self.alon1.birth_day < 29 and self.alon1.birth_month < 12)

    def test_greet(self):
        self.assertTrue()
