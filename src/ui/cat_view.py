from tkinter import Tk, ttk, constants
from entities_and_services.owner_and_cat import Owner, owner
from ui.start_view import StartView
import emoji
class CatView:
    def __init__(self, root, handle_start):
        self._root = root
        self._handle_start = handle_start
        self._frame = None
        self._owner = owner
        self.food_stat_label=None
        self.play_stat_label=None
        self._initialize()
        self._owner.owners_cat.stats_thread()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def handle_food_button_click(self):
        self._owner.feed_cat(self._owner.owners_cat)
        self.food_stat_label.config(text=f"{self._owner.owners_cat.food_percent}/100")  
        #self.update_stat_labels()
        print(self._owner.owners_cat.food_percent)

    def handle_play_button_click(self):
        self._owner.play_cat(self._owner.owners_cat)
        self.play_stat_label.config(text=f"{self._owner.owners_cat.play_percent}/100")
        print(self._owner.owners_cat.play_percent)

    def handle_return_button_click(self):
        self._owner.owners_cat.countdown=False
        self._handle_start()
    
    def update_stat_labels(self):
        self.food_stat_label.config(text=f"{self._owner.owners_cat.food_percent}/100")  
        self.play_stat_label.config(text=f"{self._owner.owners_cat.play_percent}/100")
        self._frame.after(500, self.update_stat_labels)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        name_label = ttk.Label(
            master=self._frame, 
            text=f"Nimesi on {self._owner.name}, kissasi nimi on {self._owner.owners_cat}."
        )

        food_label = ttk.Label(
            master=self._frame, 
            text="Ruoka-tarve"
            )
        self.food_stat_label = ttk.Label(
            master=self._frame,
            text=f"{self._owner.owners_cat.food_percent}/100"
            )

        play_label = ttk.Label(
            master=self._frame, 
            text="Leikki-tarve"
            )
        self.play_stat_label = ttk.Label(
            master=self._frame, 
            text=f"{self._owner.owners_cat.play_percent}/100"
            )
        cat_label = ttk.Label(
            master=self._frame,
            text="Kuva \nkissasta \ntähän"
            )
        comment_label = ttk.Label(
            master=self._frame,
            text="Kissa sanoo jotain"
        )
        food_button = ttk.Button(
            master=self._frame,
            text=f"Ruoki minua! {emoji.emojize(':face_savoring_food:')}",
            command=self.handle_food_button_click
        )
        play_button = ttk.Button(
            master=self._frame,
            text=f"Leiki kanssani! {emoji.emojize(':star-struck:')}",
            command=self.handle_play_button_click
        )

        return_button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self.handle_return_button_click
        )

        self.update_stat_labels()

        name_label.grid(row=0, column=0, columnspan=4)
        food_label.grid(row=1, column=3)
        self.food_stat_label.grid(row=1, column=4)
        play_label.grid(row=2, column=3)
        self.play_stat_label.grid(row=2, column=4)
        comment_label.grid(row=2, column=0, columnspan=3)
        cat_label.grid(row=3, column=0, columnspan=3, rowspan=3)
        food_button.grid(row=6, column=3, columnspan=2)
        play_button.grid(row=7, column=3, columnspan=2)
        return_button.grid(row=9, column=0)
