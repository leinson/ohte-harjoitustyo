#from random import randint
class Owner:
    def __init__(self):
        self.name = ""
        self.owners_cat = None

    def add_owner_name(self, owner_name):
        self.name = owner_name

    def add_cat_and_name(self, cat_name):
        new_cat = PetCat(cat_name)
        self.owners_cat = new_cat

    def feed_cat(self, cat):
        cat.stats_percent("food", 10)

    def play_cat(self, cat):
        cat.stats_percent("play", 10)

    def __str__(self):
        if self.owners_cat is None:
            return f"Käyttäjän nimi on {self.name}."
        return f"Käyttäjän nimi on {self.name}. Käyttäjän kissa on {self.owners_cat}."


class PetCat:
    def __init__(self, name):
        self.food_percent = 0  # randint(20,100)
        self.play_percent = 0
        self.name = name

    def stats_percent(self, need, percent):
        if need == "food":
            self.food_percent += percent
        if need == "play":
            self.play_percent += percent

    def __str__(self):
        return f"{self.name}"
