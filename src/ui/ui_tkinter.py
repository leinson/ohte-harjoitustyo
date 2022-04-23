#from tkinter import ttk, constants, Tk
from tkinter import *
from ui.cat_view import CatView
from ui.start_view import StartView
from ui.info_view import InfoView
from entities_and_services.owner_and_cat import Owner

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_start_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _exit_appl(self):
        # close window & exit application
        self._root.destroy()

    def _handle_cat(self):
        # move to cat view + save values somewhere
        self._show_cat_view()

    def _handle_start(self):
        # move to start view, maybe save cat stats?
        self._show_start_view()

    def _handle_info(self):
        # move to info view
        self._show_info_view()

    def _show_start_view(self):
        self._hide_current_view()

        self._current_view = StartView(
            self._root,
            self._handle_cat,
            self._handle_info,
            self._exit_appl
        )

        self._current_view.pack()

    def _show_cat_view(self):
        self._hide_current_view()

        self._current_view = CatView(
            self._root,
            self._handle_start
        )

        self._current_view.pack()

    def _show_info_view(self):
        self._hide_current_view()

        self._current_view = InfoView(
            self._root,
            self._handle_start
        )

        self._current_view.pack()


