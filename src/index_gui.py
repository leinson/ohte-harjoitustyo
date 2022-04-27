from tkinter import Tk
from ui.ui_tkinter import UI
from entities_and_services.owner_and_cat import owner


def main():

    window = Tk()
    window.title("MiukuM@uku")

    ui = UI(window)
    ui.start()

    window.mainloop()
    owner.owners_cat.countdown=False

if __name__ == '__main__':
    main()
    