from tkinter import PhotoImage, Tk, ttk, constants
from tkinter import *
from PIL import Image, ImageTk
from entities_and_services.owner_and_cat import Owner, owner
from ui.start_view import StartView
import emoji


class CatView:
    """Luokka, joka kuvastaa kissa-näkymää graafisessa käyttöliittymässä.
    """

    def __init__(self, root, handle_start):
        """Luokan konstruktori, joka luo näkymän.

        Args:
            root: GUI juuri.
            handle_start: Polku start-näkymään.
        """
        self._root = root
        self._handle_start = handle_start
        self._frame = None
        self._owner = owner
        self.food_stat_label = None
        self.play_stat_label = None
        self._cat_label = None
        self._comment_label = None
        #self.cat_image = PhotoImage(file=self._owner.owners_cat.cat_mood_img)
        self.cat_image = ImageTk.PhotoImage(
            Image.open(self._owner.owners_cat.cat_mood_img))
        self._initialize()
        self._owner.owners_cat.stats_thread()

    def pack(self):
        """Pakkaa näkymän.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän.
        """
        self._frame.destroy()

    def _handle_food_button_click(self):
        """Napinpainallus kasvattaa kissan ruokaprosenttia.
        Prosentti ei kasva, jos ruoka tai leikkiprosentti on jo alle 0,
        tai jos ruokaprosentti on liian korkea.
        """
        food_limit = self._owner.feed_cat(self._owner.owners_cat)
        if food_limit == "under_limit":
            self._comment_label.config(
                text="Karkasin jo, senkin typerys!")
        elif food_limit == "over_limit":
            self._comment_label.config(
                text="Tykkään ruuasta, mut nyt sain tarpeekseni!")
        self.food_stat_label.config(
            text=f"{self._owner.owners_cat.food_percent}/100")
        # print(self._owner.owners_cat.food_percent)

    def _handle_play_button_click(self):
        """Napinpainallus kasvattaa kissan leikkiprosenttia.
        Prosentti ei kasva, jos leikki tai ruokaprosentti on jo alle 0,
        tai jos leikkiprosentti on liian korkea.
        """
        play_limit = self._owner.play_cat(self._owner.owners_cat)
        if play_limit == "under_limit":
            self._comment_label.config(
                text="Karkasin jo, senkin typerys!")
        elif play_limit == "over_limit":
            self._comment_label.config(
                text="Hei en jaksa enää, kohta saat tassua naamaan!")

        self._owner.play_cat(self._owner.owners_cat)
        self.play_stat_label.config(
            text=f"{self._owner.owners_cat.play_percent}/100")
        # print(self._owner.owners_cat.play_percent)

    def _handle_return_button_click(self):
        """Napinpainallus siirtää käyttäjän start-näkymään.
        """
        self._owner.owners_cat.countdown = False
        self._handle_start()

    def _update_labels(self):
        """Päivittää prosentit ja kissakuvan.
        """
        self.food_stat_label.config(
            text=f"{self._owner.owners_cat.food_percent}/100")
        self.play_stat_label.config(
            text=f"{self._owner.owners_cat.play_percent}/100")

        # Kissakuvan päivittäminen ei toimi, kokeiltu PIL ja peruskuvana
        self._cat_label.configure(
            image=self.cat_image)
        self._cat_label.image = self.cat_image

        self._frame.after(500, self._update_labels)

    def _initialize(self):
        """Alustaa näkymän.
        """
        self._frame = ttk.Frame(master=self._root)
        name_label = ttk.Label(
            master=self._frame,
            text=f"Nimesi on {self._owner.name}, kissasi nimi on {self._owner.owners_cat}."
        )

        food_label = ttk.Label(
            master=self._frame,
            text="Ruoka-tarve:"
        )
        self.food_stat_label = ttk.Label(
            master=self._frame,
            text=f"{self._owner.owners_cat.food_percent}/100"
        )

        play_label = ttk.Label(
            master=self._frame,
            text="Leikki-tarve:"
        )
        self.play_stat_label = ttk.Label(
            master=self._frame,
            text=f"{self._owner.owners_cat.play_percent}/100"
        )
        self._cat_label = ttk.Label(
            master=self._frame,
            image=self.cat_image
        )
        self._comment_label = ttk.Label(
            master=self._frame,
            text="esim nam oli hyvää"
        )
        self._mood_label = ttk.Label(
            master=self._frame,
            text="esim minulla on nälkä"
        )
        food_button = ttk.Button(
            master=self._frame,
            text=f"Ruoki minua! {emoji.emojize(':face_savoring_food:')}",
            command=self._handle_food_button_click
        )
        play_button = ttk.Button(
            master=self._frame,
            text=f"Leiki kanssani! {emoji.emojize(':star-struck:')}",
            command=self._handle_play_button_click
        )

        return_button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._handle_return_button_click
        )

        self._update_labels()

        name_label.grid(row=0, column=0, columnspan=4, sticky=constants.W)
        food_label.grid(row=1, column=3, sticky=constants.W)
        self.food_stat_label.grid(row=1, column=4, sticky=constants.E, padx=25)
        play_label.grid(row=2, column=3, sticky=constants.W)
        self.play_stat_label.grid(row=2, column=4, sticky=constants.E, padx=25)
        self._comment_label.grid(
            row=3, column=3, sticky=constants.W, columnspan=2)
        self._mood_label.grid(
            row=4, column=3, sticky=constants.W, columnspan=2)
        self._cat_label.grid(row=3, column=0, columnspan=3, rowspan=3)
        food_button.grid(row=6, column=3, sticky=(
            constants.W, constants.E), columnspan=2, padx=10, pady=5)
        play_button.grid(row=7, column=3, sticky=(
            constants.W, constants.E), columnspan=2, padx=10, pady=5)
        return_button.grid(row=7, column=0, sticky=(
            constants.W, constants.E), padx=10, pady=5)
        self._frame.grid_columnconfigure(3, weight=1, minsize=150)
        self._frame.grid_columnconfigure(4, weight=1, minsize=165)
