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

    def test_no_percent_increase_if_food_over_limit(self):
        self.cat.stats_percent("food", 100)
        self.cat.stats_percent("food", 50)
        self.assertEqual(self.cat.food_percent, 120)

    def test_no_percent_increase_if_food_under_limit(self):
        self.cat.stats_percent("food", -25)
        self.cat.stats_percent("food", 50)
        self.assertEqual(self.cat.food_percent, -5)
        self.cat.stats_percent("play", 50)
        self.assertEqual(self.cat.play_percent, 20)

    def test_no_percent_increase_if_play_over_limit(self):
        self.cat.stats_percent("play", 100)
        self.cat.stats_percent("play", 50)
        self.assertEqual(self.cat.play_percent, 120)

    def test_no_percent_increase_if_play_under_limit(self):
        self.cat.stats_percent("play", -25)
        self.cat.stats_percent("play", 50)
        self.assertEqual(self.cat.play_percent, -5)
        self.cat.stats_percent("food", 50)
        self.assertEqual(self.cat.food_percent, 20)

    def test_stats_dont_decrease(self):
        self.cat.food_percent = 0
        self.cat.play_percent = 0
        self.assertEqual(self.cat.stats_decrease(), None)

    def test_stats_dont_decrease_when_countdown_false(self):
        self.cat.stats_decrease()
        self.assertEqual(self.cat.food_percent, 20)
        self.assertEqual(self.cat.play_percent, 20)

    def test_stats_decrease_when_countdown_true(self):
        self.cat.countdown = True
        self.cat._timer = 0
        self.cat.stats_decrease()
        self.assertEqual(self.cat.food_percent, -5)

    #palauta under tai over limit

    
class TestOwner(unittest.TestCase):
    def setUp(self):
        self.owner = Owner()
        self.cat = PetCat("TestCat")

    def test_name_set_correctly(self):
        self.owner.add_owner_name("Name")
        self.assertEqual(self.owner.name, "Name")

    def test_add_cat_to_owner_correctly(self):
        self.owner.add_cat_and_name("Miuku")
        self.assertEqual(self.owner.owners_cat.name, "Miuku")

    def test_if_names_are_empty_return_false(self):
        self.assertFalse(self.owner.are_names_valid("", ""))

    def test_if_names_valid_return_true(self):
        self.assertTrue(self.owner.are_names_valid("Owner", "Cat"))

    def test_feed_cat_increases_cat_stats(self):
        self.owner.feed_cat(self.cat)
        self.assertEqual(self.cat.food_percent, 30)

    def test_play_cat_increases_cat_stats(self):
        self.owner.play_cat(self.cat)
        self.assertEqual(self.cat.play_percent, 30)
