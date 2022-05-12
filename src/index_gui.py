from tkinter import Tk
from ui.ui_tkinter import UI
from entities_and_services.owner_and_cat import owner


def main():
    """Funktio, josta sovelluksen käynnistys alkaa.
    Try & except korjaa tilanteen, jossa sovellusta suljetaan ennenkuin oliota on luotu.
    """
    window = Tk()
    window.title("MiukuM@uku")
    window.geometry("800x800")
    window.configure(background="#E4D6FF")
    u_interface = UI(window)
    u_interface.start()

    window.mainloop()
    try:
        owner.owners_cat.countdown = False
    except AttributeError:
        pass


if __name__ == '__main__':
    main()
