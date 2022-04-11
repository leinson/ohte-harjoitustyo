import unittest

from classes.owner_and_cat import PetCat
from classes.owner_and_cat import Owner


class TestPetCat(unittest.TestCase):
    def setUp(self):
        self.cat = PetCat("Miuku")

    def test_name_set_correctly(self):
        self.assertEqual(self.cat.name, "Miuku")

    def test_stats_percent_increases_food_correctly(self):
        self.cat.stats_percent("food", 10)
        self.assertEqual(self.cat.food_percent, 60)

    def test_stats_percent_increases_play_correctly(self):
        self.cat.stats_percent("play", 10)
        self.assertEqual(self.cat.play_percent, 60)


class TestOwner(unittest.TestCase):
    def setUp(self):
        self.owner = Owner()

    def test_name_set_correctly(self):
        self.owner.add_owner_name("Name")
        self.assertEqual(self.owner.name, "Name")
