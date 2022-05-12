from entities_and_services.petcat import PetCat


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


owner = Owner()
