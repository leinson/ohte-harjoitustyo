import unittest

from entities_and_services.owner_and_cat import PetCat
from entities_and_services.owner_and_cat import Owner


class TestPetCat(unittest.TestCase):
    def setUp(self):
        self.cat = PetCat("Miuku")

    def test_name_set_correctly(self):
        self.assertEqual(self.cat.name, "Miuku")

    def test_stats_percent_increases_food_correctly(self):
        self.cat.stats_percent("food", 10)
        self.assertEqual(self.cat.food_percent, 30)

    def test_stats_percent_increases_play_correctly(self):
        self.cat.stats_percent("play", 10)
        self.assertEqual(self.cat.play_percent, 30)


class TestOwner(unittest.TestCase):
    def setUp(self):
        self.owner = Owner()
        self.cat = PetCat("TestCat")

    def test_name_set_correctly(self):
        self.owner.add_owner_name("Name")
        self.assertEqual(self.owner.name, "Name")
    
    def test_add_cat_to_owner_correctly(self):
        self.owner.add_cat_and_name("Miuku")
        self.assertEqual(self.owner.owners_cat.name,"Miuku" )

    def test_feed_cat_increases_cat_stats(self):
        self.owner.feed_cat(self.cat)
        self.assertEqual(self.cat.food_percent, 30)

    def test_play_cat_increases_cat_stats(self):
        self.owner.play_cat(self.cat)
        self.assertEqual(self.cat.play_percent, 30)