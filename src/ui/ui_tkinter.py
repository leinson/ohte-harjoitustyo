from ui.cat_view import CatView
from ui.start_view import StartView
from ui.info_view import InfoView


class UI:
    """Luokka, jonka avulla graafinen käyttöliittymä näkyy
    ja näkymien välillä voi siirtyä.
    """

    def __init__(self, root):
        """Luokan konstruktori, joka alustaa tyhjän näkymän.
        Args:
            root: GUI juuri.
        """
        self._root = root
        self._current_view = None

    def start(self):
        """Näyttää Start näkymän.
        """
        self._handle_start()

    def _hide_current_view(self):
        """Piilottaa eli tuhoaa nykyisen näkymän.
        """
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _exit_appl(self):
        """Tuhoaa juuren ja poistuu sovelluksesta.
        """
        self._root.destroy()

    def _handle_cat(self):
        """Siirtyy kissa-näkymään.
        """
        self._hide_current_view()

        self._current_view = CatView(
            self._root,
            self._handle_start
        )

        self._current_view.pack()

    def _handle_start(self):
        """Siirtyy start-näkymään.
        """
        self._hide_current_view()

        self._current_view = StartView(
            self._root,
            self._handle_cat,
            self._handle_info,
            self._exit_appl
        )

        self._current_view.pack()

    def _handle_info(self):
        """Siirtyy info-näkymään.
        """
        self._hide_current_view()

        self._current_view = InfoView(
            self._root,
            self._handle_start
        )

        self._current_view.pack()
