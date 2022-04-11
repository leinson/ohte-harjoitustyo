from classes.owner_and_cat import Owner
from classes.owner_and_cat import PetCat


class UserInterface:
    def __init__(self):
        self.owner = Owner()

    def instructions(self):
        print("Tämä on MiukuM@uku, virtuaalinen kissalemmikkisovellus.")
        print("Komennot:")
        print("1: Syötä oma nimesi.")
        print("2: Nimeä kissasi.")
        print("3: Syötä kissaa.")
        print("4: Leiki kissan kanssa.")
        print("5: Näytä kissan tarpeet.")
        print("0: Poistu sovelluksesta.")

    def add_owner(self):
        given_name = input("Nimi: ")
        self.owner.add_owner_name(given_name)
        print(self.owner)

    def add_cat(self):
        if self.owner.name == "":
            print("Syötä ensin oma nimesi komennolla 1.")
            return
        given_name = input("Kissan nimi: ")
        self.owner.add_cat_and_name(given_name)
        print("Kissan nimi on nyt", self.owner.owners_cat)
        print(self.owner)
        self.start_percent_decrease()

    def feeding(self):
        if self.owner.owners_cat == None:
            print("Anna ensin kissallesi nimi.")
            return
        self.owner.feed_cat(self.owner.owners_cat)
        print(f"Nam, nälkäni on nyt {self.owner.owners_cat.food_percent}/100.")

    def playing(self):
        if self.owner.owners_cat == None:
            print("Anna ensin kissallesi nimi.")
            return
        self.owner.play_cat(self.owner.owners_cat)
        print(
            f"Olipa hauskaa leikkiä! Tyytyväisyyteni on nyt {self.owner.owners_cat.play_percent}/100.")

    def show_stats(self):
        if self.check_owner_cat_not_none():
            print(
                f"Leikkimisen tarve on {self.owner.owners_cat.play_percent}/100, ruoan tarve on {self.owner.owners_cat.food_percent}/100.")
        else:
            print("Anna ensin kissallesi nimi.")

    def start_percent_decrease(self):
        self.owner.owners_cat.stats_thread()

    def check_owner_cat_not_none(self):
        if self.owner.owners_cat != None and self.owner.name != "":
            return True

    def execute(self):
        self.instructions()
        while True:
            if self.check_owner_cat_not_none():
                if self.owner.owners_cat.food_percent <= 0 or self.owner.owners_cat.play_percent <= 0:
                    break

            create_input = input("komento: ")
            if create_input == "0":
                print("Olipa kivaa, kiitos ja mau!")
                break
            if create_input == "1":
                self.add_owner()
            if create_input == "2":
                self.add_cat()
            if create_input == "3":
                self.feeding()
            if create_input == "4":
                self.playing()
            if create_input == "5":
                self.show_stats()


if False:
    user = Owner()
    user.add_owner_name("Hannah")
    user.add_cat_and_name("Miuku")
    print(user)
    print(user.owners_cat)
    print(user.owners_cat.food_percent)
    user.feed_cat(user.owners_cat)
    print(user.owners_cat.food_percent)
    user.play_cat(user.owners_cat)
    print(user.owners_cat.play_percent)
