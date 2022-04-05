import unittest
#from classes.owner_and_cat import PetCat
#from classes.owner_and_cat import Owner
from classes.owner_and_cat import PetCat
#from src import index

class TestPetCat(unittest.TestCase):
    def setUp(self):
        self.cat=PetCat("Miuku")
    
    def test_name_set_correctly(self):
        self.assertEqual(self.cat.name, "Miuku")
    
    def test_stats_percent_increases_food_correctly(self):
        self.cat.stats_percent("food", 10)
        self.assertEqual(self.cat.food_percent, 10)

