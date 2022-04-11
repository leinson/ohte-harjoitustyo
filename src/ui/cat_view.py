from tkinter import Tk, ttk, constants


class CatView:
    def __init__(self, root, handle_start):
        self._root = root
        self._handle_start = handle_start
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        name_label = ttk.Label(
            master=self._frame, text="Käyttäjän __ kissa __")
        food_label = ttk.Label(master=self._frame, text="Ruoka-tarve")
        food_stat_label = ttk.Label(master=self._frame, text="x/100")
        play_label = ttk.Label(master=self._frame, text="Leikki-tarve")
        play_stat_label = ttk.Label(master=self._frame, text="x/100")
        cat_label = ttk.Label(master=self._frame,
                              text="Kuva \nkissasta \ntähän")

        food_button = ttk.Button(
            master=self._frame,
            text="Ruoki minua!"
        )
        play_button = ttk.Button(
            master=self._frame,
            text="Leiki kanssani!"
        )

        return_button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._handle_start
        )

        name_label.grid(row=0, column=0, columnspan=4)
        food_label.grid(row=1, column=3)
        food_stat_label.grid(row=1, column=4)
        play_label.grid(row=2, column=3)
        play_stat_label.grid(row=2, column=4)
        cat_label.grid(row=2, column=0, columnspan=3, rowspan=3)
        food_button.grid(row=6, column=3, columnspan=2)
        play_button.grid(row=7, column=3, columnspan=2)
        return_button.grid(row=8, column=0)
