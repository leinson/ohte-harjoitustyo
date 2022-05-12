import unittest
from entities_and_services.petcat import PetCat


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
        self.assertEqual(self.cat._stats_decrease(), None)

    def test_stats_dont_decrease_when_countdown_false(self):
        self.cat._stats_decrease()
        self.assertEqual(self.cat.food_percent, 20)
        self.assertEqual(self.cat.play_percent, 20)

    def test_stats_decrease_when_countdown_true(self):
        self.cat.countdown = True
        self.cat.timer = 0
        self.cat._stats_decrease()
        self.assertEqual(self.cat.food_percent, -5)
    
    def test_set_difficulty_sets_timer_correctly(self):
        self.cat.set_difficulty(1)
        self.assertEqual(self.cat.timer, 10)
        self.cat.set_difficulty(2)
        self.assertEqual(self.cat.timer, 5)
        self.cat.set_difficulty(3)
        self.assertEqual(self.cat.timer, 1)

# palauta under tai over limit
