#from random import randint
import time
import threading


class Owner:
    """Luokka, joka kuvastaa yksittäistä käyttäjää. Vastaa sovelluslogiikasta.
    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden käyttäjän.
        """
        self.name = ""
        self.owners_cat = None

    def add_owner_name(self, owner_name):
        """Lisää käyttäjän nimen.

        Args:
            owner_name (string): Käyttäjän syöttämä nimi.
        """
        self.name = owner_name

    def add_cat_and_name(self, cat_name):
        """Luo kissaolion nimellä ja liittää sen omistajaan.

        Args:
            cat_name (string): Käyttäjän syöttämä kissan nimi.
        """
        new_cat = PetCat(cat_name)
        self.owners_cat = new_cat

    def feed_cat(self, cat):
        """Korottaa kissan ruokaprosenttia.

        Args:
            cat (object): omistajaan liitetty kissa-olio.
        """
        return cat.stats_percent("food", 10)

    def play_cat(self, cat):
        """Korottaa kissan leikkiprosenttia.

        Args:
            cat (object): omistajaan littetty kissa-olio.
        """
        return cat.stats_percent("play", 10)

    def __str__(self):
        """Palauttaa käyttäjän ja kissan nimet.

        Returns:
            f-string: Käyttäjän ja kissan nimet.
        """
        if self.owners_cat is None:
            return f"Käyttäjän nimi on {self.name}."
        return f"Käyttäjän {self.name} kissa {self.owners_cat}."


owner = Owner()


class PetCat:
    """Luokka, joka kuvastaa yksittäistä kissaa. Käytetään Owner luokan kautta.
    """

    def __init__(self, name):
        """Luokan konstruktori, joka luo uuden kissan ja alustaa arvot.

        Args:
            name (string): Käyttäjän syöttämä kissan nimi.
        """
        self.food_percent = 20
        self.play_percent = 20
        self.name = name
        self.countdown = False
        self._timer = 5

    def stats_percent(self, action, percent):
        """Korottaa kissan stats prosentteja määritetyn toiminnon mukaan.
        Jos jompikumpi prosenteista on alle 0,
        tai kyseisen toiminnon prosentti on liian korkea,
        ei prosentteja enää kasvateta.

        Args:
            action (string): Mitä prosentteja korotetaan
            percent (int): Minkä verran prosentteja korotetaan
        """
        if action == "food":
            if self.food_percent > 115:
                return "over_limit"
            if self.food_percent < 0:
                return "under_limit"
            if self.play_percent < 0:
                return "under_limit"
            self.food_percent += percent
        if action == "play":
            if self.play_percent > 115:
                return "over_limit"
            if self.play_percent < 0:
                return "under_limit"
            if self.food_percent < 0:
                return "under_limit"
            self.play_percent += percent

    def stats_decrease(self):
        """Alentaa kissan prosentteja tietyn aikavälin mukaan. Lopettaa ehtojen mukaan.
        """
        while self.food_percent >= 0 and self.play_percent >= 0:
            if self.countdown is True:
                self.food_percent -= 5
                self.play_percent -= 5
                time.sleep(self._timer)
            else:
                break
        if self.countdown is True:
            self.run_away()

    def stats_thread(self):
        """Aktvoi thread:in joka aloittaa ylläolevan metodin.
        """
        countdown_thread = threading.Thread(target=self.stats_decrease)
        countdown_thread.start()

    def run_away(self):
        """print tulostus, kun kissan prosentit menevät alle 0.
        """
        print(
            "Et pitänyt minusta tarpeeksi hyvää huolta. :( Karkaan naapuriin, hyvästi!")

#ei tarvita?
    def __str__(self):
        """Palauttaa kissan nimen.

        Returns:
            string: Kissan nimi.
        """
        return f"{self.name}"
