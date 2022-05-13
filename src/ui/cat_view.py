from tkinter import ttk, constants, font
from tkinter import *
from PIL import Image, ImageTk
from entities_and_services.owner import owner
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
        self._bg_color = '#E4D6FF'
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

    def _images_of_cat(self):
        """Kissakuvien alustus.
        """
        self._cat_happy_chunky = ImageTk.PhotoImage(
            Image.open("src/assets/cat_happy_chunky.png"))
        self._cat_happy_hungry = ImageTk.PhotoImage(
            Image.open("src/assets/cat_happy_hungry.png"))
        self._cat_happy = ImageTk.PhotoImage(
            Image.open("src/assets/cat_happy.png"))
        self._cat_meh_chunky = ImageTk.PhotoImage(
            Image.open("src/assets/cat_meh_chunky.png"))
        self._cat_meh_hungry = ImageTk.PhotoImage(
            Image.open("src/assets/cat_meh_hungry.png"))
        self._cat_meh = ImageTk.PhotoImage(
            Image.open("src/assets/cat_meh.png"))
        self._cat_runaway = ImageTk.PhotoImage(
            Image.open("src/assets/cat_runaway.png"))
        self._cat_sad_chunky = ImageTk.PhotoImage(
            Image.open("src/assets/cat_sad_chunky.png"))
        self._cat_sad_hungry = ImageTk.PhotoImage(
            Image.open("src/assets/cat_sad_hungry.png"))
        self._cat_sad = ImageTk.PhotoImage(
            Image.open("src/assets/cat_sad.png"))
        self._cat_sweaty_chunky = ImageTk.PhotoImage(
            Image.open("src/assets/cat_sweaty_chunky.png"))
        self._cat_sweaty_hungry = ImageTk.PhotoImage(
            Image.open("src/assets/cat_sweaty_hungry.png"))
        self._cat_sweaty = ImageTk.PhotoImage(
            Image.open("src/assets/cat_sweaty.png"))

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
        else:
            self._comment_label.config(
                text=f"Nam, olipa hyvää! {emoji.emojize(':face_savoring_food:')}")

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
        else:
            self._comment_label.config(
                text=f"Jee leikkiminen on kivaa! {emoji.emojize(':grinning_face_with_smiling_eyes:')}")

    def _handle_return_button_click(self):
        """Napinpainallus siirtää käyttäjän start-näkymään.
        """
        self._owner.owners_cat.countdown = False
        self._handle_start()

    def _change_cat_mood(self):
        """Päivittää kissakuvan ja mood-tekstikentän prosenttien mukaan.
        """
        if self._owner.owners_cat.play_percent < 0 or self._owner.owners_cat.food_percent < 0:
            self._cat_label.configure(image=self._cat_runaway)
            self._cat_label.image = self._cat_runaway

        elif self._owner.owners_cat.play_percent > 100:
            if self._owner.owners_cat.food_percent > 100:
                self._cat_label.configure(image=self._cat_sweaty_chunky)
                self._cat_label.image = self._cat_sweaty_chunky
                self._mood_label.config(text="")
            elif self._owner.owners_cat.food_percent >= 50:
                self._cat_label.configure(image=self._cat_sweaty)
                self._cat_label.image = self._cat_sweaty
                self._mood_label.config(text="")
            else:
                self._cat_label.configure(image=self._cat_sweaty_hungry)
                self._cat_label.image = self._cat_sweaty_hungry
                self._mood_label.config(text=f"Ihan hirvee nälkä! {emoji.emojize(':weary_face:')}")

        elif self._owner.owners_cat.play_percent >= 70:
            if self._owner.owners_cat.food_percent > 100:
                self._cat_label.configure(image=self._cat_happy_chunky)
                self._cat_label.image = self._cat_happy_chunky
                self._mood_label.config(text="")
            elif self._owner.owners_cat.food_percent >= 50:
                self._cat_label.configure(image=self._cat_happy)
                self._cat_label.image = self._cat_happy
                self._mood_label.config(text="")
            else:
                self._cat_label.configure(image=self._cat_happy_hungry)
                self._cat_label.image = self._cat_happy_hungry
                self._mood_label.config(
                    text=f"Ihan hirvee nälkä! {emoji.emojize(':weary_face:')}")

        elif self._owner.owners_cat.play_percent >= 30:
            if self._owner.owners_cat.food_percent > 100:
                self._cat_label.configure(image=self._cat_meh_chunky)
                self._cat_label.image = self._cat_happy_chunky
                self._mood_label.config(text="")
            elif self._owner.owners_cat.food_percent >= 50:
                self._cat_label.configure(image=self._cat_meh)
                self._cat_label.image = self._cat_happy
                self._mood_label.config(text="")
            else:
                self._cat_label.configure(image=self._cat_meh_hungry)
                self._cat_label.image = self._cat_meh_hungry
                self._mood_label.config(
                    text=f"Ihan hirvee nälkä! {emoji.emojize(':weary_face:')}")
        else:
            if self._owner.owners_cat.food_percent > 100:
                self._cat_label.configure(image=self._cat_sad_chunky)
                self._cat_label.image = self._cat_sad_chunky
                self._mood_label.config(
                    text=f"Hei leikitäänkö, pliis {emoji.emojize(':crying_face:')}")
            elif self._owner.owners_cat.food_percent >= 50:
                self._cat_label.configure(image=self._cat_sad)
                self._cat_label.image = self._cat_sad
                self._mood_label.config(
                    text=f"Hei leikitäänkö, pliis {emoji.emojize(':crying_face:')}")
            else:
                self._cat_label.configure(image=self._cat_sad_hungry)
                self._cat_label.image = self._cat_sad_hungry
                self._mood_label.config(
                    text=f"Tilanne SOS, ruokaa ja leikkimistä heti!! {emoji.emojize(':face_with_crossed-out_eyes:')}")

    def _update_labels(self):
        """Päivittää prosentit ja kissakuvan.
        """
        self._food_stat_label.config(
            text=f"{self._owner.owners_cat.food_percent} / 100")
        self._play_stat_label.config(
            text=f"{self._owner.owners_cat.play_percent} / 100")
        self._change_cat_mood()
        self._frame.after(50, self._update_labels)

    def _initialize(self):
        """Alustaa näkymän.
        """
        self._images_of_cat()
        _font = font.Font(family='Quicksand', size=12)
        _font_large = font.Font(family='Quicksand', size=14)

        self._frame = ttk.Frame(master=self._root)

        name_label = ttk.Label(
            master=self._frame,
            text=f"Nimesi on {self._owner.name}, kissasi nimi on {self._owner.owners_cat.name}.",
            font=_font_large,
            background=self._bg_color
        )
        food_label = ttk.Label(
            master=self._frame,
            text="Ruoka-tarve:",
            font=_font,
            background=self._bg_color
        )
        self._food_stat_label = ttk.Label(
            master=self._frame,
            text=f"{self._owner.owners_cat.food_percent}/100",
            font=_font_large,
            background=self._bg_color
        )
        play_label = ttk.Label(
            master=self._frame,
            text="Leikki-tarve:",
            font=_font,
            background=self._bg_color
        )
        self._play_stat_label = ttk.Label(
            master=self._frame,
            text=f"{self._owner.owners_cat.play_percent}/100",
            font=_font_large,
            background=self._bg_color
        )
        self._cat_label = ttk.Label(
            master=self._frame,
            image=self._cat_meh,
            background=self._bg_color
        )
        self._comment_label = ttk.Label(
            master=self._frame,
            text="",
            font=_font,
            background=self._bg_color
        )
        self._mood_label = ttk.Label(
            master=self._frame,
            text="",
            font=_font,
            background=self._bg_color
        )
        food_button = ttk.Button(
            master=self._frame,
            text=f"Ruoki minua! {emoji.emojize(':face_savoring_food:')}",
            command=self._handle_food_button_click
        )
        play_button = ttk.Button(
            master=self._frame,
            text=f"Leiki kanssani! {emoji.emojize(':grinning_face_with_smiling_eyes:')}",
            command=self._handle_play_button_click
        )
        return_button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._handle_return_button_click
        )

        name_label.grid(
            row=0, column=0, columnspan=4,
            sticky=constants.W, 
            pady=40, padx=30
        )
        food_label.grid(
            row=1, column=3, 
            sticky=constants.W
        )
        self._food_stat_label.grid(
            row=1, column=4, 
            sticky=(constants.W, constants.E), 
            padx=25
        )
        play_label.grid(
            row=2, column=3, 
            sticky=constants.W, 
            pady=10
        )
        self._play_stat_label.grid(
            row=2, column=4, 
            sticky=(constants.W, constants.E), 
            padx=25, pady=10
        )
        self._mood_label.grid(
            row=3, column=3, columnspan=2,
            sticky=constants.W,
        )
        self._comment_label.grid(
            row=5, column=3, columnspan=2,
            sticky=constants.W
        )
        self._cat_label.grid(
            row=3, column=0, 
            columnspan=3, rowspan=3, 
            padx=30
        )
        food_button.grid(
            row=6, column=3, 
            sticky=(constants.W, constants.E), 
            padx=10, pady=5, ipady=5
        )
        play_button.grid(
            row=6, column=4, 
            sticky=(constants.W, constants.E), 
            padx=10, pady=10, ipady=5
        )
        return_button.grid(
            row=6, column=0, sticky=(constants.W, constants.E), 
            padx=30, pady=10, ipady=5
        )
        self._frame.grid_columnconfigure(
            3, weight=1, minsize=150
        )
        self._frame.grid_columnconfigure(
            4, weight=1, minsize=165
        )

        self._update_labels()
