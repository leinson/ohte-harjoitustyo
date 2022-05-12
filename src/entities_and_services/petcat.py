import time
import threading


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
        self.timer = None

    def set_difficulty(self, level):
        """Asettaa kissan timerin käyttäjän valitseman vaikeustason mukaan.
        Args:
            level: helppo=1, keskivaikea=2, vaikea=3
        """
        if level == 1:
            self.timer = 10
        elif level == 2:
            self.timer = 5
        else:
            self.timer = 1

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
            if self.food_percent > 100:
                return "over_limit"
            if self.food_percent < 0:
                return "under_limit"
            if self.play_percent < 0:
                return "under_limit"
            self.food_percent += percent
        if action == "play":
            if self.play_percent > 100:
                return "over_limit"
            if self.play_percent < 0:
                return "under_limit"
            if self.food_percent < 0:
                return "under_limit"
            self.play_percent += percent

    def stats_thread(self):
        """Aktvoi thread:in joka aloittaa ylläolevan metodin.
        """
        countdown_thread = threading.Thread(target=self._stats_decrease)
        countdown_thread.start()

    def _stats_decrease(self):
        """Alentaa kissan prosentteja valitseman vaikeustason mukaan. Lopettaa ehtojen mukaan.
        """
        while self.food_percent >= 0 and self.play_percent >= 0:
            if self.countdown is True:
                self.food_percent -= 5
                self.play_percent -= 5
                time.sleep(self.timer)
            else:
                break
