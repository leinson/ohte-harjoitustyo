#from random import randint
class Owner:
    def __init__(self):
        self.name=""
        self.owners_cat= None
     
    def add_owner_name(self,owner_name):
        self.name=owner_name

    def add_cat_and_name(self, cat_name):
        new_cat= PetCat(cat_name)
        self.owners_cat=new_cat
    
    def feed_cat(self, cat):
        cat.stats_percent("food", 10)

    def play_cat(self, cat):
        cat.stats_percent("play", 10)

    def __str__(self):
        if self.owners_cat==None:
            return f"Käyttäjän nimi on {self.name}."
        else:
            return f"Käyttäjän nimi on {self.name}. Käyttäjän kissa on {self.owners_cat}."

class PetCat:
    def __init__(self, name):
        self.food_percent= 0 #randint(20,100)
        self.play_percent= 0
        self.name=name 

    def stats_percent(self, need, percent):
        if need=="food":
            self.food_percent+=percent
        if need=="play":
            self.play_percent+=percent

    def __str__(self):
        return f"{self.name}"



class UserInterface:
    def __init__(self):
        self.owner= Owner()

    def instructions(self):
        print("Tämä on MiukuM@uku, virtuaalinen kissalemmikkisovellus.") 
        print("Komennot:")
        print("1: Syötä oma nimesi.")
        print("2: Nimeä kissasi.")
        #print("3: Syötä kissaa.")
        #print("4: Leiki kissan kanssa.")
        print("0: Poistu sovelluksesta.")

    def add_owner(self):
        given_name= input("Nimi: ")
        self.owner.add_owner_name(given_name)
        print(self.owner)

    def add_cat(self):
        if self.owner.name=="":
            print("Syötä ensin oma nimesi komennolla 1.")
            return
        given_name= input("Kissan nimi: ")
        self.owner.add_cat_and_name(given_name)
        print("Kissan nimi on nyt", self.owner.owners_cat)
        print(self.owner)

    def feeding(self):
        if self.owner.owners_cat==None:
            print("Anna ensin kissallesi nimi.")
            return
        self.owner.feed_cat(self.owner.owners_cat)
        print(f"Nam, nälkäni on nyt {self.owner.owners_cat.food_percent}/100.")

    def execute(self):
        self.instructions()
        while True:
            create_input= input("komento: ")
            if create_input== "0":
                break
            if create_input=="1":
                self.add_owner()
            if create_input=="2":
                self.add_cat()
            if create_input=="3":
                self.feeding()



the_program= UserInterface()
the_program.execute()

if False:
    user= Owner()
    user.add_owner_name("Hannah")
    user.add_cat_and_name("Miuku")    
    print(user)
    print(user.owners_cat)
    print(user.owners_cat.food_percent)
    user.feed_cat(user.owners_cat)
    print(user.owners_cat.food_percent)
    user.play_cat(user.owners_cat)
    print(user.owners_cat.play_percent)