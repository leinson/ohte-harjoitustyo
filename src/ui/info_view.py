from tkinter import Tk, ttk, constants


class InfoView:
    """Luokka, joka kuvastaa Ohjeet näkymää graafisessa käyttöliittymässä.
    """

    def __init__(self, root, handle_start):
        """Luokan konstruktori, joka luo näkymän.

        Args:
            root: GUI juuri.
            handle_start: Reitti millä palataan start näkymään
        """
        self._root = root
        self._handle_start = handle_start
        self._frame = None

        self._initialize()

    def pack(self):
        """Pakkaa näkymän.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän.
        """
        self._frame.destroy()

    def _initialize(self):
        """Alustaa luokan ja näkymän.
        """
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Info")

        button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._handle_start
        )

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)
