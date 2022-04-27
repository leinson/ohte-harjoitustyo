#from random import randint
import time
import threading



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
        return f"Käyttäjän {self.name} kissa {self.owners_cat}."

owner=Owner()


class PetCat:
    def __init__(self, name):
        self.food_percent = 20  # randint(20,100)
        self.play_percent = 20
        self.name = name
        self.countdown = False

    def stats_percent(self, action, percent):
        if action == "food":
            self.food_percent += percent
        if action == "play":
            self.play_percent += percent

    def stats_decrease(self): #ei lopu oikein koska uusi parametri ei välity samaan funktiokutsuun
        while self.food_percent > 0 and self.play_percent > 0:
            if self.countdown == True:
                self.food_percent -= 5
                self.play_percent -= 5
                time.sleep(5)
            else:
                break
        if self.countdown==True:
            self.run_away()

    def stats_thread(self):
        countdown_thread = threading.Thread(target=self.stats_decrease)
        countdown_thread.start()

    def run_away(self):
        print("Et pitänyt minusta tarpeeksi hyvää huolta. :( Karkaan naapuriin, hyvästi!")

    def __str__(self):
        return f"{self.name}"
