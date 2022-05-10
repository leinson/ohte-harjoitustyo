from tkinter import StringVar, ttk, constants
from entities_and_services.owner_and_cat import Owner, owner
import emoji


class StartView:
    """Luokka, joka kuvastaa aloitusnäkymää graafisessa käyttöliittymässä.
    """

    def __init__(self, root, handle_cat, handle_info, exit_appl):
        """Luokan konstruktori, joka luo näkymän.

        Args:
            root: GUI juuri.
            handle_cat: Polku Kissa-näkymään.
            handle_info: Polku Ohjeet-näkymään
            exit_appl: Polku sovelluksen sulkemiseen napilla.
        """
        self._root = root
        self._handle_cat = handle_cat
        self._handle_info = handle_info
        self._exit_appl = exit_appl
        self._frame = None
        self._entry_user = None
        self._entry_cat = None
        self.owner = None
        self.comment_label = None
        self._initialize()

    def pack(self):
        """Pakkaa näkymän.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän.
        """
        self._frame.destroy()

    def _handle_start_button_click(self):
        """Luo Owner ja PetCat oliot käyttäjän syöttämien tietojen mukaan
        ja siirtyy Kissa-näkymään jos nimet eivät ole tyhjiä.
        """
        self.owner = owner
        entry_value_user = self._entry_user.get()
        entry_value_cat = self._entry_cat.get()
        if self.are_names_valid(entry_value_user, entry_value_cat) is False:
            self._update_comment_label()
        else:
            self.owner.add_owner_name(entry_value_user)
            self.owner.add_cat_and_name(entry_value_cat)
            self.owner.owners_cat.countdown = True
            self._handle_cat()

    def are_names_valid(self, owner_name, cat_name):
        if owner_name == "" or cat_name == "":
            return False
        return True

    def _update_comment_label(self):
        """Päivittää kommenttikentän.
        """

        self.comment_label.config(
            text="Syötä ensin oma nimesi ja kissasi nimi.")

    def _initialize(self):
        """Alustaa näkymän.
        """
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame,
            text="Tämä on MiukuM@uku, virtuaalinen kissalemmikkisovellus.\nLuethan ohjeet, ennen kuin aloitat.\n\nSyötä tiedot alle:"
        )
        user_label = ttk.Label(
            master=self._frame,
            text="Nimesi:"
        )
        self._entry_user = ttk.Entry(
            master=self._frame,
            textvariable=StringVar()
        )

        cat_label = ttk.Label(
            master=self._frame,
            text="Kissan nimi:"
        )
        self._entry_cat = ttk.Entry(
            master=self._frame,
            textvariable=StringVar()
        )

        start_button = ttk.Button(
            master=self._frame,
            text=f"Aloita! {emoji.emojize(':cat_face:')}",
            command=self._handle_start_button_click
        )

        info_button = ttk.Button(
            master=self._frame,
            text="Ohjeet",
            command=self._handle_info
        )
        exit_button = ttk.Button(
            master=self._frame,
            text="Poistu",
            command=self._exit_appl
        )
        self.comment_label = ttk.Label(
            master=self._frame,
            text=f""
        )

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=15)
        user_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        self._entry_user.grid(row=1, column=1, sticky=(
            constants.W, constants.E), padx=5, pady=5)
        cat_label.grid(row=2, column=0, sticky=constants.W, padx=5, pady=5)
        self._entry_cat.grid(row=2, column=1, sticky=(
            constants.W, constants.E), padx=5, pady=5)
        info_button.grid(row=3, column=0, sticky=constants.W, padx=5, pady=15)
        start_button.grid(row=3, column=1, sticky=(
            constants.W, constants.E), padx=5, pady=5)
        exit_button.grid(row=4, column=0, sticky=constants.W, padx=5, pady=5)
        self.comment_label.grid(row=4, column=1, sticky=(constants.W))
        self._frame.grid_columnconfigure(1, weight=1, minsize=400)
